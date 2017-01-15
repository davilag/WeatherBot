import telepot
from weather_consumer.weather_service import WeatherService

class MessageConsumer(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(MessageConsumer, self).__init__(*args, **kwargs)
        self._weather_service = WeatherService()

    def on_chat_message(self, msg):
        try:
            content_type, chat_type, chat_id = telepot.glance(msg)
        except:
            #TODO(davilag): need to add some logging in order to detect which messages are failing.
            e = sys.exc_info()[0]
            print( "Error: %s" % e )

        if content_type == 'location':
            response = self._weather_service.build_today_forecast_response(msg)
            self.sender.sendMessage(response)
