import telebot
from dotenv import load_dotenv
import os

def get_token():
    load_dotenv("token.env")
    return os.environ.get('TOKEN')

API_TOKEN = get_token()
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напишіть ID товару для пошуку.")