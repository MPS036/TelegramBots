import os
import time
import telebot

INTERVAL = 300  # seconds
CHANNEL_NAME = "@channel"

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set.")

bot = telebot.TeleBot(token)

def load_jokes():
    with open("data/jokes.txt", encoding="utf-8") as f:
        return [line for line in f.read().splitlines() if line.strip()]

def autopost():
    jokes = load_jokes()

    if not jokes:
        print("No jokes found.")
        return

    print(f"Starting autopost. {len(jokes)} messages loaded.")

    for joke in jokes:
        try:
            bot.send_message(CHANNEL_NAME, joke)
            print("Sent:", joke[:30])
            time.sleep(INTERVAL)
        except Exception as e:
            print("Error sending message:", e)
            time.sleep(10)

if __name__ == "__main__":
    autopost()
