"""
A-or-B Telegram Bot (Facts / Jokes) {or whatever you want}

A simple Telegram bot that shows two buttons (e.g., "Joke" and "Fact").
When a user presses a button, the bot sends a random line from a
corresponding text file.

Requirements:
- Environment variable: BOT_TOKEN
- Data files:
  - data/jokes.txt (one joke per line)
  - data/facts.txt (one fact per line)
"""

import os
import random
import telebot
from telebot import types

JOKES_PATH = "data/jokes.txt"
FACTS_PATH = "data/facts.txt"

def load_lines(path: str) -> list[str]:
    """
    Load non-empty lines from a UTF-8 text file.

    Args:
        path: Path to a text file.

    Returns:
        List of stripped, non-empty lines. Returns an empty list if the file
        does not exist.
    """
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f.read().splitlines() if line.strip()]

jokes = load_lines(JOKES_PATH)
facts = load_lines(FACTS_PATH)

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set. Create .env or export BOT_TOKEN environment variable.")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message) -> None:
    """
    Send a welcome message and show the category buttons.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Joke")
    item2 = types.KeyboardButton("Fact")
    markup.add(item1, item2)

    bot.send_message(
        message.chat.id,
        "Press:\nJoke — to get an interesting joke\nFact — to get a funny fact",
        reply_markup=markup,
    )

@bot.message_handler(content_types=["text"])
def handle_text(message) -> None:
     """
    Handle text messages.

    - If the user selects "Joke" -> send a random joke
    - If the user selects "Fact" -> send a random fact
    - Otherwise -> ask the user to use buttons
    """
    text = message.text.strip().lower()

    if text == "joke":
        answer = random.choice(jokes) if jokes else "Jokes list is empty."
    elif text == "fact":
        answer = random.choice(facts) if facts else "Facts list is empty."
    else:
        answer = "Please use the buttons: Joke / Fact 🙂"

    bot.send_message(message.chat.id, answer)

if __name__ == "__main__":
    bot.infinity_polling()
