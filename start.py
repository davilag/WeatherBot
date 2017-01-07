from WeatherConsumer.WeatherConsumer import WeatherConsumer
from WeatherConsumer.ResponseConstructor import WeatherResponseConstructor
import telepot, time, os

#Method to handle all the messages from the clients.
def handle (msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
    elif content_type == 'location':

        location = _getMessageLocation(msg)
        weatherInfo = weatherConsumer.getForecastByLatLon(location['lat'], location['lon'])

        response = responseConstructor.buildActualWeatherResponse(weatherInfo, msg['date'])
        bot.sendMessage(chat_id, response)

def _getMessageLocation(msg):
    location = msg['location']
    return {'lat': str(location['latitude']), 'lon': str(location['longitude'])}

print('Starting bot')

weatherConsumer = WeatherConsumer()
responseConstructor = WeatherResponseConstructor()
bot = telepot.Bot(os.getenv('TELEGRAM_API_TOKEN', ''))

bot.message_loop(handle)

while 1:
    time.sleep(10)
