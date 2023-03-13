import tkinter as tk
import weatherstation

window = tk.Tk()

window.title("Wacky Weather Station")
window.geometry("800x480")

# Create the background image
background_image = tk.PhotoImage(file="newclouds.gif")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# City entry box
entry = tk.Entry(window)
entry.place(x=40, y=50)

window.mainloop()
