import os

import telebot
from dotenv import load_dotenv

from func1 import search_product_by_id
from func2 import send_welcome
from func4 import handle_message

print("privit")

def get_token():
    load_dotenv()
    return os.environ.get('TOKEN')

API_TOKEN = get_token()
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    send_welcome(message)


def deco(func):
    def wrapper():
        func()
        print("Бот запустився")
    return wrapper


@deco
def main():
    @bot.message_handler(commands=['start'])
    def start_welcome(message):
        send_welcome(message)

    @bot.message_handler(func=lambda message: True)
    def id_product(message):
        product_id = message.text.strip()
        response_message = search_product_by_id(product_id)
        bot.reply_to(message, response_message)

    @bot.message_handler(func=lambda message: True)
    def handle(message):
        handle_message(message)



if __name__ == "__main__":
    main()

bot.polling()
