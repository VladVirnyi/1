import telebot
from func_1 import search_product_by_id
from task7 import get_token

API_TOKEN = get_token()
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    product_id = message.text.strip()
    response_message = search_product_by_id(product_id)
    bot.reply_to(message, response_message) 

bot.polling()
