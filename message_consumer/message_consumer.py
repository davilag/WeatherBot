import telepot
from weather_consumer.weather_service import WeatherService

class MessageConsumer(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(MessageConsumer, self).__init__(*args, **kwargs)
        self._weather_service = WeatherService()
        self._actions = {'/rain': self._send_rain_forecast}
        self._command = None
        self._arguments = None

    def on_chat_message(self, msg):
        try:
            content_type, chat_type, chat_id = telepot.glance(msg)
        except:
            #TODO(davilag): need to add some logging in order to detect which messages are failing.
            e = sys.exc_info()[0]
            print( "Error: %s" % e )

        if content_type == 'location':
            if not self._command:
                response = self._weather_service.build_today_forecast_response(msg)
            else:
                response = self._actions[self._command](msg)
            self.sender.sendMessage(response)
        elif content_type == 'text':
            print('I get a text')
            self._command, self._arguments = self._get_command_arguments(msg['text'])
            if self._command and self._actions[self._command]:
                self.sender.sendMessage('Now send your location')

    def _get_command_arguments(self, msg):
        msg = msg.strip()
        if msg.startswith('/'):
            ms = msg.split(' ')
            return ms[0], ms[1::]
        return None, None

    def _send_rain_forecast(self, msg):
        self._command = None
        self._arguments = None

        date = None
        if not self._arguments:
            date = msg['date']

        if date :
            return self._weather_service.build_rain_forecast_response(msg)
        else:
            return 'Didnt get that bit'
