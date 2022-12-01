import telebot
import time

bot = telebot.TeleBot('token')
CHANNEL_NAME = '@channel'

f = open('path/jokes.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    time.sleep(300)

bot.send_message(CHANNEL_NAME, "Nothing to send")
