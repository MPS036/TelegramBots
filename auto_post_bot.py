"""
Telegram Auto-Post Bot

A simple automation script that sends messages from a text file
to a specified Telegram channel at fixed time intervals.

Requirements:
- Environment variable: BOT_TOKEN
- data/jokes.txt (one message per line) {or whatever you want}
- Bot must be added as admin to the target channel
"""

import os
import time
import telebot

INTERVAL = 300  # seconds
CHANNEL_NAME = "@channel" # Replace with your channel username

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set.")

bot = telebot.TeleBot(token)

def load_messages(path: str = "data/jokes.txt") -> list[str]:
    """
    Load non-empty lines from a text file.

    Args:
        path: Path to the file containing messages.

    Returns:
        List of messages (one per line).
    """
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return []

    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f.read().splitlines() if line.strip()]


def autopost() -> None:
     """
    Send messages sequentially to the Telegram channel
    with a fixed delay between each message.
    """
    messages = load_messages()

    if not messages:
        print("No messages found.")
        return

    print(f"Starting autopost. {len(messages)} messages loaded.")
    print(f"Posting to: {CHANNEL_NAME}")
    print(f"Interval: {INTERVAL} seconds")

    for message in messages:
        try:
            bot.send_message(CHANNEL_NAME, message)
            print("Sent:", message[:30])
            time.sleep(INTERVAL)
        except Exception as e:
            print("Error sending message:", e)
            time.sleep(10)

if __name__ == "__main__":
    autopost()
