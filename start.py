from weather_consumer.weather_service import WeatherService
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
        response = weather_service.build_today_forecast_response(msg)
        bot.sendMessage(chat_id, response)

print('Starting bot')

weather_service = WeatherService()
bot = telepot.Bot(os.getenv('TELEGRAM_API_TOKEN', ''))

bot.message_loop(handle)

while 1:
    time.sleep(10)
