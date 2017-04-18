# sample02.py : add label in GUI windows

from tkinter import *

# create windows
root = Tk()

# modified root wondows
root.title("CopyLE125code")
root.geometry("400x200")

#add this to show content in GUI
app = Frame(root)
app.grid()

#add label
label = Label(app, text = "Test Labeller")
label.grid()

# kick off the event loop
root.mainloop()
