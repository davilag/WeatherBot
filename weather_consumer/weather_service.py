import datetime
from .weather_consumer import WeatherConsumer

class WeatherService:

    def __init__(self):
        self.__weather_consumer = WeatherConsumer()

    def build_today_forecast_response (self, msg):

        location = self.__get_message_location(msg)
        weather_api_response = self.__weather_consumer.get_forecast_by_lat_lon(location['lat'], location['lon'])

        message_timestamp = msg['date']
        todays_forecast = self.__get_forecast_by_date(weather_api_response['daily']['data'], message_timestamp)[0]
        if not todays_forecast:
            return 'No forecast found!'

        actual_weather = weather_api_response['currently']
        out = ("The weather in your location is:\n"
              "{}\n"
              "🔺 Max temperature: {} ºC\n"
              "🔻 Min temperature: {} ºC\n"
              "🕑 Actual temperature: {} ºC\n"
              "☂️ Rain probability: {}%").format(todays_forecast['summary'],
                                                 round(todays_forecast['temperatureMax']),
                                                 round(todays_forecast['temperatureMin']),
                                                 round(actual_weather['temperature']),
                                                 round(actual_weather['precipProbability'] * 100))
        return out

    def build_rain_forecast_response (self, msg):
        date = msg['date']
        location = self.__get_message_location(msg)

        weather_api_response = self.__weather_consumer.get_hourly_details_by_lat_lon(location['lat'], location['lon'])

        rain_forecast = self.__get_forecast_by_date(weather_api_response['hourly']['data'], date)

        rl = self.__get_rain_hours(rain_forecast)

        if not rl:
            return 'It\'s not going to rain'

        out = 'Rain probability\n'
        for r in rl:
            out += ('{}:\t{}%\n').format(r['hour'], r['prob'])

        return out


    #Gets the forecast given the message date and checking if the
    def __get_forecast_by_date(self, daily_response, message_timestamp):

        out = []
        message_date = message_timestamp

        for forecast in daily_response:
            forecast_date = datetime.datetime.fromtimestamp(forecast['time'])
            if (forecast_date.day == message_date.day and
                forecast_date.month == message_date.month and
                forecast_date.year == message_date.year):

                out.append(forecast)

        return out

    def __get_message_location (self, msg):
        location = msg['location']
        return {'lat': str(location['latitude']), 'lon': str(location['longitude'])}

    def __get_rainy_hours (self, f):
        out = []

        for fh in f:
            if f['precipIntensity'] > 0:
                out.append(fh)

        return out
    def __get_rain_hours (self, items):
        o = []
        for item in items:
            hour = datetime.datetime.fromtimestamp(item['time']).hour
            precipProbability = round(item['precipProbability'] * 100)
            if precipProbability:
                o.append({'hour': ('{}h - {}h').format(hour, hour + 1), 'prob': precipProbability})

        return o
