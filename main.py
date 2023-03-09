from weatherstation import *

print("Wacky Weather Station 1.0")

while True:
    city = get_city()
    temperature = get_temperature(city)

    print("The current temperature of ", city, "is ", temperature)

