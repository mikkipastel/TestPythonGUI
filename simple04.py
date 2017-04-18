# how to use OOP for GUI with tkinter

from tkinter import *

class Application(Frame):
  #have 3 button in this
  
  def __init__(self, master):
    # initialize frame
    Frame.__init__(self, master)
    self.grid()
    self.create_widgets()
    
  def create_widgets(self):
    #create 3 button
    self.button1 = Button(self, text = "1st button")
    self.button1.grid()
    
    self.button2 = Button(self)
    self.button2.grid()
    self.button2.configure(text = "2nd button")
    
    self.button3 = Button(self)
    self.button3.grid()
    self.button3["text"] = "3rd button"

#for debug
if __name__=="__main__":
  root = Tk()
  root.title("Labeller")
  root.geometry("200x85")

  app = Application(root)

  root.mainloop()
