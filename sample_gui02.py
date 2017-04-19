from tkinter import *
from tkinter.ttk import *

class Application(Frame):
  def __init__(self, master):
    # initialize frame
    Frame.__init__(self, master)
    self.grid()
    self.create_widgets()
    
  def create_widgets(self):
  
    # add Entry
    self.entry = Entry(self, width=20)
    self.entry.grid(column=0, row=1)
    
    # add Radiobutton
    eimer_mc = [("chicken", "chicken"), ("pork", "pork"), ("meat", "meat")]
    cnt = 1
    for text, mode in eimer_mc:
      self.radio = Radiobutton(self, text=text, variable=var, value=mode, width=5)
      self.radio.grid(column=cnt, row=1)
      cnt+=1
      
    # add button
    self.button = Button(self)
    self.button.grid()
    self.button["text"] = "Print"
    self.button["command"] = self.copy_eimer
    self.button.grid(column=2, row=2)
    
  # print input
  def copy_eimer(self):
    print(self.entry.get(), var.get())

# for debug
if __name__=="__main__":
  root = Tk()
  root.title("Lebeller")
  root.geometry("350x200")

  var = StringVar()
  
  app = Application(root)

  root.mainloop()
