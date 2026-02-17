import os
from dataclasses import dataclass
import telebot
from fuzzywuzzy import fuzz

THRESHOLD = 80
DATA_PATH = "bot_data/chat.txt"
LOG_DIR = "bot_data"

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set. Create .env or export BOT_TOKEN environment variable.")

bot = telebot.TeleBot(token)


@dataclass
class QA:
    question: str
    answer: str


def load_qa(path: str) -> list[QA]:
    """
    Expects chat.txt format like:
    u: hello
    b: hi
    u: how are you
    b: fine
    """
    if not os.path.exists(path):
        return []

    qa_list: list[QA] = []
    last_question: str | None = None

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if len(line) < 3:
                continue

            low = line.lower()

            if low.startswith("u:"):
                last_question = line[2:].strip().lower()
            elif low.startswith("b:") and last_question:
                answer = line[2:].strip()
                qa_list.append(QA(question=last_question, answer=answer))
                last_question = None

    return qa_list


QA_DATA = load_qa(DATA_PATH)


def get_answer(text: str) -> str:
    text = text.lower().strip()
    if not text:
        return "Say something 🙂"

    if not QA_DATA:
        return "Chat database is empty. Please add phrases to bot_data/chat.txt"

    best_score = -1
    best_answer = None

    for qa in QA_DATA:
        score = fuzz.token_sort_ratio(qa.question, text)
        if score > best_score:
            best_score = score
            best_answer = qa.answer

    if best_score >= THRESHOLD and best_answer:
        return best_answer

    return "I don't know how to answer that yet 😅"


def log_dialog(chat_id: int, user_text: str, bot_text: str) -> None:
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"{chat_id}_log.txt")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"u: {user_text}\n")
        f.write(f"b: {bot_text}\n\n")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "I am here — say hello to me!")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    reply = get_answer(message.text)
    log_dialog(message.chat.id, message.text, reply)
    bot.send_message(message.chat.id, reply)


if __name__ == "__main__":
    bot.infinity_polling()
