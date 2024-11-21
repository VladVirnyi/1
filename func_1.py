import requests
import telebot

API_TOKEN = '7439201277:AAHufghwh9NHBph5ZFdFJfjBldrACQfHZEQ'
bot = telebot.TeleBot(API_TOKEN)

def search_product_by_id(product_id):
    url = f'https://common-api.rozetka.com.ua/v2/goods/get-price/?country=UA&lng=ua&ids={product_id}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        try:
            data = response.json()

            if isinstance(data, list):
                if len(data) > 0:
                    product = data[0]

                    product_price = product.get('price', 'Ціна не вказана')

                    product_url = f"https://rozetka.com.ua/ua/search/?text={product.get('id', '')}"

                    product_title = product.get('title', None)

                    if product_title:
                        result = f"Товар знайдено:\n" \
                                 f"Назва: {product_title}\n" \
                                 f"Ціна: {product_price}\n" \
                                 f"Посилання: {product_url}"
                    else:
                        result = f"Товар знайдено:\n" \
                                 f"Ціна: {product_price}\n" \
                                 f"Посилання: {product_url}"

                    return result
                else:
                    return "Товар не знайдено за вказаним ID."
            else:
                return "Невідомий формат відповіді API. Очікувався список."

        except ValueError:
            return "Не вдалося розпарсити JSON."

    except requests.exceptions.RequestException as e:
        return f"Помилка при запиті до Rozetka: {e}"
    except Exception as e:
        return f"Сталася помилка: {e}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напишіть ID товару для пошуку.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    product_id = message.text.strip()
    response_message = search_product_by_id(product_id)
    bot.reply_to(message, response_message)

bot.polling()
