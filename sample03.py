# sample03.py : add button

from tkinter import *

# create windows
root = Tk()

# modified root wondows
root.title("Lebeller")
root.geometry("400x200")

# add this to show content in GUI
app = Frame(root)
app.grid()

# add button
button1 = Button(app, text = "Button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "show text")

button3 = Button(app)
button3.grid()
button3['text'] = "test"

# kick off the event loop
root.mainloop()
