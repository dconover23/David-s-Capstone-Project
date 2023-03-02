# weather.py: Contains all the important weather-accessing stuff.
import requests
import json

api_key = "32244071f3e58861bea8ab0d64ef14b5"

# "Base" URL to initialize with
base_url = "http://api.openweathermap.org/data/2.5/weather?"


class Weather:
    def __init__(self, city):
        self.city = city

    # Gets the city and all relevant API info
    def getCity(self, city_name):
        city_name = self.city

        # Finish the URL
        complete_url = base_url + "appid=" + api_key + "&q" + city_name

        # Send URL to API
        response = requests.get(complete_url)

        # Results come back in json
        result = response.json()

        # Make sure API is up
        if result["cod"] != 404:
            main = result["main"]

            # Get current temperature
            current_temp = main["temp"]

            # Convert it to fahrenheit from kelvin
            current_temperature = round((current_temp - 273.15) * 1.8 + 32)

            return current_temperature

