import requests
import os
import json

class WeatherConsumer:

    _apiUrl = os.getenv('WEATHER_API_URL', '')
    _apiToken = os.getenv('WEATHER_API_TOKEN', '')

    # Constructor
    def __init__ (self):
        if not self._apiUrl or not self._apiToken:
            raise Exception('Could not initialize WeatherConsumer.')

    def getForecastByLatLon (self, lat, lon):
        payload = {'lat' : lat, 'lon' : lon}
        requestURL = self._apiUrl + self._apiToken + '/' + lat + ',' + lon
        return self._makeForecastRequest(requestURL)

    def _makeForecastRequest (self, requestURL):
        requestParams = {'units' : 'si', 'exclude' : 'minutely,hourly,flags' }
        request = requests.get(requestURL, params = requestParams)
        responseDictionary = json.loads(request.text)
        return responseDictionary
