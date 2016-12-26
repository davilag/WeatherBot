
from WeatherConsumer.Consumer import WeatherConsumer

print('Starting bot')

weatherConsumer = WeatherConsumer()
print(weatherConsumer.getForecastByLatLon('38.852565', '-3.772717'))
