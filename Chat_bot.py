import telebot
import os
from fuzzywuzzy import fuzz

bot = telebot.TeleBot('token')

mas=[]
if os.path.exists('bot_data/chat.txt'):
    f = open('bot_data/chat.txt', 'r', encoding = 'UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()

def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('bot_data/chat.txt'):
            a = 80
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if aa > a:
                          nn = n
                          s = mas[nn+1]
                          break
                    else:
                        s = '0'
                        n = n + 1
            return s
    except:
        return 'Error'

@bot.message_handler(commands = ["start"])
def start(m, res = False):
        bot.send_message(m.chat.id, 'I am here, say Hello to me')

@bot.message_handler(content_types = ["text"])
def handle_text(message):

    f = open('bot_data/' + str(message.chat.id) + '_log.txt', 'a', encoding = 'UTF-8')
    s = answer(message.text)
    f.write('u: ' + message.text + '\n' + s +'\n')
    f.close()
    if str(s) != '0':
		bot.reply_to(message, s)
		
    bot.send_message(message.chat.id, s)

bot.polling(none_stop = True, interval = 0)
