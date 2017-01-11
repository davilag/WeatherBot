import requests, os, json

class WeatherConsumer:

    __api_url = os.getenv('WEATHER_API_URL', '')
    __api_token = os.getenv('WEATHER_API_TOKEN', '')

    # Constructor
    def __init__ (self):
        if not self.__api_url or not self.__api_url:
            raise Exception('Could not initialize WeatherConsumer.')

    # Gets the forecas for the next week given a latitude and longitude.
    def get_forecast_by_lat_lon (self, lat, lon):
        request_url = '{}{}/{},{}'.format(self.__api_url, self.__api_token, lat, lon)
        return self.__make_forecast_request(request_url)

    # Makes the request to the weather API adding parameters for the units and
    # unused response information.
    def __make_forecast_request (self, request_url):
        request_params = {'units' : 'si', 'exclude' : 'minutely,hourly,flags' }
        request = requests.get(request_url, params = request_params)
        response_dictionary = json.loads(request.text)
        return response_dictionary
