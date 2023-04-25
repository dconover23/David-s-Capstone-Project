# weatherstation.py: Contains all the important weather-accessing stuff.
import requests
import RPi.GPIO as GPIO
from time import sleep

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

blue = GPIO.PWM(17, 60)    # create object red for PWM on port 17
green = GPIO.PWM(27, 60)      # create object green for PWM on port 27
red = GPIO.PWM(22, 60)      # create object blue for PWM on port 22

# Pin setup for wind dir servo
GPIO.setup(26, GPIO.OUT)
servo = GPIO.PWM(26, 50)

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
        set_servo_position(wind_direction)
    else:
        wind_direction = None

    return wind_direction

def set_servo_position(wind_direction):
    servo.start(0)
    # Set servo position based on wind direction
    if 22.5 <= wind_direction < 67.5:
        servo.ChangeDutyCycle(6.25)  # 45 degrees (northeast)
    elif 67.5 <= wind_direction < 112.5:
        servo.ChangeDutyCycle(7.5)  # 90 degrees (east)
    elif 112.5 <= wind_direction < 157.5:
        servo.ChangeDutyCycle(8.75)  # 135 degrees (southeast)
    elif 157.5 <= wind_direction < 202.5:
        servo.ChangeDutyCycle(12.5)  # 180 degrees (south)
    elif 202.5 <= wind_direction < 247.5:
        servo.ChangeDutyCycle(15)  # 225 degrees (southwest)
    elif 247.5 <= wind_direction < 292.5:
        servo.ChangeDutyCycle(17.5)  # 270 degrees (west)
    elif 292.5 <= wind_direction < 337.5:
        servo.ChangeDutyCycle(1.25)  # 315 degrees (northwest)
    else:
        servo.ChangeDutyCycle(0)  # 0 degrees (north)


