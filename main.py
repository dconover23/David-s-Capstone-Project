import tkinter as tk
import weatherstation

window = tk.Tk()
# Tutorial shouldn't be opened unless the user asks for it
tutorial = tk.Toplevel(window)
tutorial.withdraw()

window.title("Wacky Weather Station")
window.geometry("800x480")
window.resizable(False, False)

tutorial.title("Help")
tutorial.resizable(False, False)

# Create the background image
background_image = tk.PhotoImage(file="newclouds.gif")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the Tkinter vars so that the information display can automatically update
tempDisplay = tk.IntVar(window, 0)
windDirDisplay = tk.StringVar(window, "")
# Initialized outside of try...except block to avoid UnboundLocalError
windDir_label = tk.Label(window, text="")
weather_label = tk.Label(window, text="")

# The tutorial window that is opened when the help button is pressed.
def openTutorial():
    tutorialtext = tk.Label(tutorial, "Type a city into the prompt to get the temp and wind speed of that location. "
                                      "If you want to be precise with the location, use the format [City, "
                                      "Country/State].")
    tutorialtext.pack()

# This will submit the user's input to the API when the corresponding button is pressed. It also clears the label
# in case it already hasn't to make space for any new city the user submits.
def getWeatherWithEntry():
    user_input = entry.get()

    if user_input != "":
        # get the temperature for the user's choice of city...
        temperature = weatherstation.get_temperature(user_input)
        tempDisplay.set(temperature)
        weather_label = tk.Label(window, text="")
        weather_label = tk.Label(window, text=f"{tempDisplay.get()} degrees Fahrenheit")

        # ...and do the same for wind direction.
        windDirection = weatherstation.get_wind_direction(user_input)
        windDirDisplay.set(windDirection)
        windDir_label = tk.Label(window, text="")
        windDir_label = tk.Label(window, text=f"{windDirDisplay.get()} is the current wind direction (in degrees)")

        weather_label.place(x=500, y=120)
        windDir_label.place(x=500, y=160)


# Create the entry box for inputting city
entry = tk.Entry(window)
entry.place(x=40, y=20)

# Create the button for confirming the input
button = tk.Button(window, text="Subvert Big Weather", command=getWeatherWithEntry)
button.place(x=40, y=60)

window.mainloop()
