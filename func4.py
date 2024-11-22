import telebot
from func1 import search_product_by_id
from dotenv import load_dotenv
import os

def get_token():
    load_dotenv()
    return os.environ.get('TOKEN')

API_TOKEN = get_token()
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    product_id = message.text.strip()
    response_message = search_product_by_id(product_id)
    bot.reply_to(message, response_message)
