import telebot
bot = telebot.TeleBot('5816106402:AAHU7vrm-mv_gP8BM9Unlr5bqvx5EOOqx84')
@bot.message_handler(commands = ["start"])
def start(m, res = False):
    bot.send_message(m.chat.id, 'I am here, type something')
@bot.message_handler(content_types = ["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'You wrote: ' + message.text)
bot.polling(none_stop = True, interval = 0)
