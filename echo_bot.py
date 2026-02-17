import os
import telebot

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN is not set. Create .env or export BOT_TOKEN environment variable.")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hi! I am Echo Bot.\nSend me any text and I will repeat it back to you."
    )


@bot.message_handler(content_types=["text"])
def echo(message):
    text = message.text.strip()

    if not text:
        bot.reply_to(message, "Please send some text 🙂")
        return

    bot.reply_to(message, f"You wrote: {text}")


if __name__ == "__main__":
    bot.infinity_polling()
