import tkinter as tk
from weather import *

window = tk.Tk()
window.title("Wacky Weather Station: Hacky Prototype Edition")
window.geometry("740x640")

label = tk.Label(text="Enter a City")
entry = tk.Entry(bg="lightgrey", width=50)

label.pack()
entry.pack()

window.mainloop()
