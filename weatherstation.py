# weatherstation.py: Contains all the important weather-accessing stuff.
import requests
import RPi.GPIO as GPIO

# Pin setup

in1 = 29
in2 = 23 
en = 31

# LED
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Motor
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
motor = GPIO.PWM(en,1000)


# Pin setup for LED
blue = GPIO.PWM(11, 60)    
green = GPIO.PWM(13, 60)      
red = GPIO.PWM(15, 60)      

# You need your own API key from OpenWeatherMap. Google "OpenWeatherMap API key".
api_key = "INSERT-YOUR-OWN-API-KEY-HERE"

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

        # Initialize the pins
        red.stop()
        green.stop()
        blue.stop()

        # The RGB LED's color changes based on temp. Blue is very cold, red is very hot!
        if current_temperature >= 100:
            # Very hot, set to red
            red.start(100)
            green.start(0)
            blue.start(0)
        elif current_temperature < 100 and current_temperature >= 70:
            # Warm, set to yellow
            red.start(100)
            green.start(100)
            blue.start(0)
        elif current_temperature < 70 and current_temperature >= 40:
            # Mild, set to green
            red.start(0)
            green.start(100)
            blue.start(0)
        elif current_temperature < 40 and current_temperature >= 20:
            # Cold, set to blue
            red.start(0)
            green.start(0)
            blue.start(100)
        else:
            # Very cold, set to white
            red.start(100)
            green.start(100)
            blue.start(100)

        return current_temperature


# Gets wind direction of specified city
# TODO: Hook the motor up to this
def get_wind_direction(city):

    # Complete URL for OpenWeatherMap API
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    # Fire off request to API
    response = requests.get(complete_url)

    # The data we get back from the API
    result = response.json()

    if result["cod"] != "404":
        wind = result["wind"]
        wind_direction_degrees = wind["deg"]
        wind_direction = wind_direction_degrees
        degrees = wind_direction

        directions = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]

        # Split into the available directions
        degrees = degrees * len(directions) / 360

        # Round it to avoid weird decimal answers
        degrees = round(degrees)

        if 0 <= degrees < len(directions):
            degrees = directions[degrees]

            # Test motor
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
        else:
            degrees = None

        return degrees

