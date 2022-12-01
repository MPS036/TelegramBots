import telebot
import random
from telebot import types

#Let's look at an example on a joke and a fact

f = open('path/jokes.txt', 'r', encoding = 'UTF-8')
facts = f.read().split('\n')
f.close

f = open('path/facts.txt', 'r', encoding = 'UTF-8')
facts = f.read().split('\n')
f.close

bot = telebot.TeleBot('token/api key from telegram')

@bot.message_handler(commands = ["start"])
def start(m, res = False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Joke")
        item2=types.KeyboardButton("Fact")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Press: \nJoke to get an intersting Joke\nFact to get a funny Fact\n ',  reply_markup=markup)

@bot.message_handler(content_types = ["text"])
def handle_text(message):
    if message.text.strip() == 'Joke':
        answer = random.choice()
    elif message.text.strip() == 'Fact':
        answer = random.choice()
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True, interval = 0)
