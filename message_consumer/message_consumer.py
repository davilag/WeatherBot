from weather_consumer.weather_service import WeatherService
from telegram import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

class MessageConsumer:
    def __init__(self, *args, **kwargs):
        self._weather_service = WeatherService()

    def get_rain_handler(self):
        flow = self.RainForecastFlow()
        return flow.conv_handler

    def today_forecast(self, msg):
        return self._weather_service.build_today_forecast_response(msg)

    class RainForecastFlow:

        def __init__(self):
            self._weather_service = WeatherService()
            self._LOCATION = range(1)
            self.conv_handler = ConversationHandler(
                entry_points=[CommandHandler('rain', self._start)],

                states={
                    self._LOCATION: [MessageHandler(Filters.location, self._location)]
                },

                fallbacks=[CommandHandler('cancel', self._cancel)]
            )

        def _start(self, bot, update):
            location_keyboard = KeyboardButton(text='Send location', request_location=True)
            custom_keyboard = [[ location_keyboard ]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard)
            update.message.reply_text('Would you mind sharing your location with me?',
                                reply_markup=reply_markup)
            return self._LOCATION

        def _location(self, bot, update):
            update.message.reply_text(self._weather_service.build_rain_forecast_response(update['message']),
                                        reply_markup=ReplyKeyboardRemove())
            return ConversationHandler.END

        def _cancel(self, bot, update):
            return ConversationHandler.END
