from tkinter import *
from tkinter.ttk import *

class Application(Frame):
  def __init__(self, master):
    # initialize frame
    Frame.__init__(self, master)
    self.grid()
    self.create_widgets()
    
  def create_widgets(self):
  
    #add label for number
    self.label1 = Label(self)
    self.label1["text"] = "Number :" 
    self.label1.grid(column=1, row=2)
    
    # create combobox for select number
    self.box = Combobox(self)
    self.box['values'] = ('1', '2', '3', '4', '5')
    self.box.current(0)
    self.box.bind("<<>ComboboxSelected>")
    self.box.grid(column=2, row=2)

    # create print button
    self.button = Button(self)
    self.button["text"] = "Print"
    self.button["command"] = self.print_number
    self.button.grid(column=2, row=3)
    
  # copy source file from eimer to destination folder
  def print_number(self):
    print("hi there, everyone! " + self.box.get())

# for debug
if __name__=="__main__":
  root = Tk()
  root.title("Lebeller")
  root.geometry("350x200")

  app = Application(root)

  root.mainloop()
