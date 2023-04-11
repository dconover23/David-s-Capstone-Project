# weatherstation.py: Contains all the important weather-accessing stuff.
import requests
import RPi.GPIO as GPIO

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

red = GPIO.PWM(17, 60)    # create object red for PWM on port 17
green = GPIO.PWM(27, 60)      # create object green for PWM on port 27
blue = GPIO.PWM(22, 60)      # create object blue for PWM on port 22

api_key = "3ec252c41ca3ab7db6eb8f63408bed10"

# "Base" URL to initialize with
base_url = "http://api.openweathermap.org/data/2.5/weather?"

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

        if current_temperature > 1:
            red.start(255)
            green.start(0)
            blue(0)
        else:
            # Otherwise, turn off the LED
            red.start(0)
            green.start(255)
            blue.start(0)

        return current_temperature

# Gets wind direction of specified city
def get_wind_direction(city):

    # Complete URL for OpenWeatherMap API
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    # Fire off request to API
    response = requests.get(complete_url)

    # The data we get back from the API
    result = response.json()

    # Get wind direction for servo
    if result["cod"] != "404":
        wind = result["wind"]
        wind_direction_degrees = wind["deg"]
        wind_direction = wind_direction_degrees


    return wind_direction
