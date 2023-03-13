import tkinter as tk
import weatherstation

window = tk.Tk()

window.title("Wacky Weather Station")
window.geometry("800x480")
window.resizable(False, False)

# Create the background image
background_image = tk.PhotoImage(file="newclouds.gif")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def getWeatherWithEntry():
    user_input = entry.get()
    if user_input != "":
        temperature = weatherstation.get_temperature(user_input)
        print("The current temp is", temperature)
    else:
        print("You need to enter a valid city.")

# Create the entry box for inputting city
entry = tk.Entry(window)
entry.place(x=40, y=20)

# Create the button for confirming the input
button = tk.Button(window, text="Subvert Big Weather", command=getWeatherWithEntry)
button.place(x=40, y=60)

window.mainloop()
