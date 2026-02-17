import os
import random
import telebot
from telebot import types

with open("data/jokes.txt", encoding="utf-8") as f:
    jokes = f.read().splitlines()

with open("data/facts.txt", encoding="utf-8") as f:
    facts = f.read().splitlines()

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set. Create .env or export BOT_TOKEN environment variable.")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
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
def handle_text(message):
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
