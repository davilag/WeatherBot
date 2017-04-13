import requests, os, json

class WeatherConsumer:

    # Constructor
    def __init__ (self):
        self.__api_url = os.getenv('WEATHER_API_URL', '')
        self.__api_token = os.getenv('WEATHER_API_TOKEN', '')
        if not self.__api_url or not self.__api_url:
            raise Exception('Could not initialize WeatherConsumer.')

    # Gets the forecas for the next week given a latitude and longitude.
    def get_forecast_by_lat_lon (self, lat, lon):
        request_url = '{}{}/{},{}'.format(self.__api_url, self.__api_token, lat, lon)
        return self.__make_api_request(request_url, 'minutely,hourly,flags')

    def get_hourly_details_by_lat_lon(self, lat, lon):
        request_url = '{}{}/{},{}'.format(self.__api_url, self.__api_token, lat, lon)
        return self.__make_api_request(request_url, 'minutely,daily,flags')

    # Makes the request to the weather API adding parameters for the units and
    # unused response information.
    def __make_api_request (self, request_url, exclude):
        request_params = {'units' : 'si', 'exclude' : exclude }
        request = requests.get(request_url, params = request_params)
        response_dictionary = json.loads(request.text)
        return response_dictionary
