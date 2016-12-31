class WeatherResponseConstructor:

    def buildActualWeatherResponse (self, weatherApiResponse):
        out = 'The weather in your location is:\n'

        #The response returns always the day before as the first value in the
        #daily forecast.
        todaysForecast = weatherApiResponse['daily']['data'][1]

        actualWeather = weatherApiResponse['currently']
        out += todaysForecast['summary'] + '\n'
        out += 'Max temperature: ' + str(int(round(todaysForecast['temperatureMax']))) + 'ºC\n'
        out += 'Min temperature: ' + str(int(round(todaysForecast['temperatureMin']))) + 'ºC\n'
        out += 'Actual temperature: ' + str(int(round(actualWeather['temperature']))) + 'ºC'

        return out
