import datetime

class WeatherResponseConstructor:

    def buildActualWeatherResponse (self, weatherApiResponse, messageTimestamp):
        out = 'The weather in your location is:\n'

        todaysForecast = self._getForecastByDate(weatherApiResponse['daily']['data'], messageTimestamp)

        if not todaysForecast:
            return 'No forecast found!'

        actualWeather = weatherApiResponse['currently']
        out += todaysForecast['summary'] + '\n'
        out += 'Max temperature: ' + str(int(round(todaysForecast['temperatureMax']))) + 'ºC\n'
        out += 'Min temperature: ' + str(int(round(todaysForecast['temperatureMin']))) + 'ºC\n'
        out += 'Actual temperature: ' + str(int(round(actualWeather['temperature']))) + 'ºC'

        return out

    #Gets the forecast given the message date and checking if the
    def _getForecastByDate(self, dailyResponse, messageTimestamp):
        messageDate = datetime.datetime.fromtimestamp(messageTimestamp)
        print(messageDate)

        for forecast in dailyResponse:
            forecastDate = datetime.datetime.fromtimestamp(forecast['time'])

            if (forecastDate.day == messageDate.day and
                forecastDate.month == messageDate.month and
                forecastDate.year == messageDate.year):

                return forecast

        return None
