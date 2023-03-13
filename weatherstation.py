# weatherstation.py: Contains all the important weather-accessing stuff.
import requests


# TODO: Figure out why API request is 401'ing
api_key = "3ec252c41ca3ab7db6eb8f63408bed10"

# "Base" URL to initialize with
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_city():
    city = input("Enter a city name: ")
    return city

def get_temperature(city):
    # Complete URL for OpenWeatherMap API
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    # Fire off request to API
    response = requests.get(complete_url)

    # The data we get back from the API
    result = response.json()

    if result["cod"] != "404":
        main = result["main"]
        current_temp = main["temp"]

        current_temperature = round((current_temp - 273.15) * 1.8 + 32)
        return current_temperature

def get_wind_direction(city):
    # Complete URL for OpenWeatherMap API
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    # Fire off request to API
    response = requests.get(complete_url)

    # The data we get back from the API
    result = response.json()

    # If-elif hell to get the wind direction for the servos
    if result["cod"] != "404":
        wind = result["wind"]
        wind_direction_degrees = wind["deg"]
        if wind_direction_degrees >= 348.75 or wind_direction_degrees < 11.25:
            wind_direction = "N"
        elif wind_direction_degrees >= 33.75 and wind_direction_degrees < 56.25:
            wind_direction = "NE"
        elif wind_direction_degrees >= 78.75 and wind_direction_degrees < 101.25:
            wind_direction = "E"
        elif wind_direction_degrees >= 123.75 and wind_direction_degrees < 146.25:
            wind_direction = "SE"
        elif wind_direction_degrees >= 168.75 and wind_direction_degrees < 191.25:
            wind_direction = "S"
        elif wind_direction_degrees > 202.5 and wind_direction_degrees <= 247.5:
            wind_direction = "SW"
        elif wind_direction_degrees >= 258.75 and wind_direction_degrees < 281.25:
            wind_direction = "W"
        elif wind_direction_degrees >= 303.75 and wind_direction_degrees < 326.25:
            wind_direction = "NW"
