import requests
from pprint import pprint

api_key = '13032cae1afa9b3f93e94a0236118989'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?units=metric&appid=" + api_key + "&q=" + city #WEATHER
# base_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&units=metric&appid=" + api_key + "&q=" + city #COMPLETE FORECASTS

weather_data = requests.get(base_url).json()

pprint(weather_data)