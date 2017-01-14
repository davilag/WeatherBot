from .weather_consumer import WeatherConsumer
import datetime

class WeatherService:

    __weather_consumer = WeatherConsumer()

    def build_today_forecast_response (self, msg):

        location = self.__get_message_location(msg)
        weather_api_response = self.__weather_consumer.get_forecast_by_lat_lon(location['lat'], location['lon'])

        message_timestamp = msg['date']
        todays_forecast = self.__get_forecast_by_date(weather_api_response['daily']['data'], message_timestamp)

        if not todays_forecast:
            return 'No forecast found!'

        actual_weather = weather_api_response['currently']
        out = ("The weather in your location is:\n"
              "{}\n"
              "Max temperature: {} ºC\n"
              "Min temperature: {} ºC\n"
              "Actual temperature: {} ºC").format(todays_forecast['summary'],
                                                 round(todays_forecast['temperatureMax']),
                                                 round(todays_forecast['temperatureMin']),
                                                 round(actual_weather['temperature']))
        return out

    #Gets the forecast given the message date and checking if the
    def __get_forecast_by_date(self, daily_response, message_timestamp):
        message_date = datetime.datetime.fromtimestamp(message_timestamp)

        for forecast in daily_response:
            forecast_date = datetime.datetime.fromtimestamp(forecast['time'])

            if (forecast_date.day == message_date.day and
                forecast_date.month == message_date.month and
                forecast_date.year == message_date.year):

                return forecast

        return None

    def __get_message_location(self, msg):
        location = msg['location']
        return {'lat': str(location['latitude']), 'lon': str(location['longitude'])}
