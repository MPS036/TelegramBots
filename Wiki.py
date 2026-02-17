import os
import re
import telebot
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError, WikipediaException

MAX_TG_MESSAGE = 4096
DEFAULT_LANG = os.getenv("WIKI_LANG", "de")

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set. Create .env or export BOT_TOKEN environment variable.")

bot = telebot.TeleBot(token)
wikipedia.set_lang(DEFAULT_LANG)


def clean_text(text: str) -> str:
    # Remove parenthesis/brackets content and curly braces templates
    text = re.sub(r"\([^()]*\)", "", text)
    text = re.sub(r"\{[^{}]*\}", "", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def getwiki(query: str, limit_chars: int = 1200) -> str:
    q = query.strip()
    if not q:
        return "Type a topic to search 🙂"

    try:
        page = wikipedia.page(q, auto_suggest=True, redirect=True)
        raw = page.content[:limit_chars]

        # Keep only sentence-like parts, drop section markers
        parts = raw.split(".")
        out_parts = []
        for p in parts:
            p = p.strip()
            if not p or "==" in p:
                continue
            out_parts.append(p)
            if len(". ".join(out_parts)) > limit_chars:
                break

        result = ". ".join(out_parts).strip()
        if result and not result.endswith("."):
            result += "."

        result = clean_text(result)

        if not result:
            return "I found a page, but couldn't extract a clean preview."

        # Telegram hard limit
        if len(result) > MAX_TG_MESSAGE:
            result = result[: MAX_TG_MESSAGE - 1]

        return result

    except DisambiguationError as e:
        # show a few options
        options = e.options[:8]
        return "Too many results. Try one of these:\n- " + "\n- ".join(options)

    except PageError:
        return "No page found for this query. Try a different keyword."

    except WikipediaException:
        return "Wikipedia error occurred. Please try again later."

    except Exception:
        return "Unexpected error. Please try again later."


@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Send me a topic and I’ll return a short Wikipedia preview.\n"
        f"Current language: {DEFAULT_LANG}\n"
        f"Tip: you can set WIKI_LANG in .env (e.g., de/en/ru).",
    )


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


if __name__ == "__main__":
    bot.infinity_polling()
