from weatherstation import *

print("Wacky Weather Station")

while True:
    city = get_city()
    temperature = get_temperature(city)

    print("The current temperature of ", city, "is ", temperature)

