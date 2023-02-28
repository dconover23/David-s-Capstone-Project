import tkinter as tk

window = tk.Tk()
window.title("Wacky Weather Station: Hacky Prototype Edition")
window.geometry("1024x768")

label = tk.Label(text = "Enter a City")
entry = tk.Entry(bg="lightgrey", width=50)

label.pack()
entry.pack()

window.mainloop()
