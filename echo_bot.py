"""
Echo Telegram Bot

A minimal Telegram bot that replies with the same text
sent by the user.

Purpose:
(i) Demonstrate basic usage of Telegram Bot API
(ii) Show command and message handlers
(iii) Provide a minimal working bot example

Requirements:
(i) Environment variable: BOT_TOKEN
(ii) Dependency: pytelegrambotapi
"""

import os
import telebot

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set. Create .env or export BOT_TOKEN environment variable.")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def start(message) -> None:
    """
    Handle /start and /help commands.

    Sends a short description of the bot.
    """
    bot.send_message(
        message.chat.id,
        "Hi! I am Echo Bot.\nSend me any text and I will repeat it back to you."
    )

@bot.message_handler(content_types=["text"])
def echo(message) -> None:
      """
    Echo back any text message sent by the user.

    Args:
        message: Telegram message object.
    """
    text = message.text.strip()

    if not text:
        bot.reply_to(message, "Please send some text 🙂")
        return

    bot.reply_to(message, f"You wrote: {text}")

if __name__ == "__main__":
    bot.infinity_polling()
