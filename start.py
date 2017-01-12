from weather_consumer.weather_consumer import WeatherConsumer
from weather_consumer.response_constructor import WeatherResponseConstructor
import telepot, time, os

#Method to handle all the messages from the clients.
def handle (msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)
    except:
        #TODO(davilag): need to add some logging in order to detect which messages are failing.
        e = sys.exc_info()[0]
        print( "Error: %s" % e )

    if content_type == 'location':

        location = _get_message_location(msg)
        weatherInfo = weather_consumer.get_forecast_by_lat_lon(location['lat'], location['lon'])

        response = response_constructor.build_actual_weather_response(weatherInfo, msg['date'])
        bot.sendMessage(chat_id, response)

def _get_message_location(msg):
    location = msg['location']
    return {'lat': str(location['latitude']), 'lon': str(location['longitude'])}

print('Starting bot')

weather_consumer = WeatherConsumer()
response_constructor = WeatherResponseConstructor()
bot = telepot.Bot(os.getenv('TELEGRAM_API_TOKEN', ''))

bot.message_loop(handle)

while 1:
    time.sleep(10)
