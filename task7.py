import requests
import telebot
from func_1 import search_product_by_id
from func_2 import send_welcome
from func_3 import handle_message
from dotenv import load_dotenv
import os

def get_token():
    load_dotenv()
    return os.environ.get('TOKEN')

API_TOKEN = get_token()
bot = telebot.TeleBot(API_TOKEN)

def deco(func):
    def wrapper():
        # print("Бот запустився")  # Повідомлення до запуску функції
        func()  # Викликає основну функцію
        print("Бот запустився")
    return wrapper

@deco
def main():
    search_product_by_id()
    send_welcome()
    handle_message()

if __name__ == "__main__":
    main()

bot.polling()
