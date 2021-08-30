import telebot
token = '1948450134:AAGAmwYNHc838aclNjtTA1t1DWq6554ppfU'
bot = telebot.TeleBot(token)
def repeat_all_messages():
    bot.send_message(523442794, 'hello world!')
repeat_all_messages()
