from WeatherConsumer.WeatherConsumer import WeatherConsumer
from WeatherConsumer.ResponseConstructor import WeatherResponseConstructor
import telepot
import time
import os

print('Starting bot')

weatherConsumer = WeatherConsumer()
responseConstructor = WeatherResponseConstructor()
bot = telepot.Bot(os.getenv('TELEGRAM_API_TOKEN', ''))

def handle (msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
    elif content_type == 'location':
        location = msg['location']
        weatherInfo = weatherConsumer.getForecastByLatLon(location['latitude'], location['longitude'])
        bot.sendMessage(chat_id, responseConstructor.buildActualWeatherResponse(weatherInfo))

bot.message_loop(handle)

while 1:
    time.sleep(10)
