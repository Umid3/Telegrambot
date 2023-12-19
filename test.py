from contextvars import Token
import telebot
import configparser
token = "734274982:AAHscFNqwOIaIRaxxHUZ6KAZY12-OEI5cDI";

bot = telebot.TeleBot(configparser, Token)
@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text'])

def func(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(non_stop=True)

