# import the necessary modules
import requests
from pprint import pprint

# get the API key
API_Key = input('Enter the API key:')
# get the city name you want to look into
city = input('Enter a city/country: ')

base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=' + API_Key + '&q=' + city

weather_data = requests.get(base_url).json()

pprint(weather_data)

data = input("\nEnter the specific field name (weather, wind, etc.) you want to see: ")

try:
    pprint(f"{data}: {weather_data[data]}")
except:
    print('Exiting!')
    exit()