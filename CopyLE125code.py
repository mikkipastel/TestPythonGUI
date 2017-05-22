#------------------------------------------------------------------------------#
# file name   : CopyLE125code.py                                               #
# version     : 1.0                                                            #
# description : Copy eimer source file to test in LE125 project                #
# parameters  : eimer_path, folder_destination, file_mc, filename              #
#------------------------------------------------------------------------------#
# Modification History:                                                        #
# Date:       Name:         V:   Change Description:                           #
# 18.04.2017  Monthira Ch   1.0  First version                                 #
#------------------------------------------------------------------------------#

#import GUI library
from tkinter import *
from tkinter.ttk import *

#import default library
import os
import sys
import shutil
import codecs

class Application(Frame):
  
  def __init__(self, master):
    # initialize frame
    Frame.__init__(self, master)
    self.grid()
    self.create_widgets()
    
  def create_widgets(self):
    # [1] add label frame for folder
    self.label1 = LabelFrame(self, text="Folder ")
    self.label1.grid(row=0, columnspan=7, sticky='WE', \
            padx=5, pady=5, ipadx=25, ipady=5)
    
    # [1.1] add label for eimer folder
    self.label_source = Label(self.label1, width=15)
    self.label_source.grid(column=0, row=2, sticky='E', padx=5, pady=5)
    self.label_source["text"] = "eimer path :"
    
    # [1.2] add Entry (EditText) to get eimer path
    self.entry_eimer = Entry(self.label1, width=50)
    self.entry_eimer.grid(column=1, row=2, sticky='E', padx=5, pady=5)
    
    # [1.3] add label for destination folder
    self.label_dest = Label(self.label1, width=15)
    self.label_dest.grid(column=0, row=3, sticky='E', padx=5, pady=5)
    self.label_dest["text"] = "destination path :"
    
    # [1.4] add Entry (EditText) to get eimer path
    self.entry_dest = Entry(self.label1, width=50)
    self.entry_dest.grid(column=1, row=3, sticky='E', padx=5, pady=5)
    
    # [2] add label frame for filename
    self.label2 = LabelFrame(self, text="File ")
    self.label2.grid(row=4, columnspan=7, sticky='WE', \
             padx=5, pady=5, ipadx=25, ipady=5)
    
    # [2.1] create Radiobutton to choose mc0 or mc2
    self.label_dest = Label(self.label2, width=15)
    self.label_dest.grid(column=0, row=5, sticky='E', padx=5, pady=5)
    self.label_dest["text"] = "eimer mc :"
    
    eimer_mc = [("mc0", "mc0"), ("mc2", "mc2")]
    cnt = 1
    for text, mode in eimer_mc:
      self.radio = Radiobutton(self.label2, text=text, variable=var, value=mode, width=5)
      self.radio.grid(column=cnt, row=5)
      cnt+=1
    
    # [2.2] add label for combobox
    self.label_filename = Label(self.label2, width=15)
    self.label_filename["text"] = "file Name :"  
    self.label_filename.grid(column=0, row=6, sticky='E', padx=5, pady=5)
    
    # [2.3] create combobox for select file name
    self.box = Combobox(self.label2)
    #self.box.grid()
    self.box['values'] = ("fgbdrv.c", "Flayer_DPR_put_mc0.c", "Flayer_DPR_put_mc2.c", \
        "fslayer.c", "fslayer_cps_hvsm0.c", "fslayer_cps_hvsm2.c", "fslayer_dispatcher.c", "fu2.c", \
        "lbts2.c", "mgu0_uewquad.c", "mwrs2.c", "tgt2.c", "zfm0.c", "zket.c")
    #self.box.current(0)
    self.box.bind("<<>ComboboxSelected>")
    self.box.grid(column=1, row=6)

    # [3] create copy file button
    self.button = Button(self)
    #self.button.grid()
    self.button["text"] = "Copy"
    self.button["command"] = self.copy_eimer
    self.button.grid(column=2, row=8)
  
  # copy source file from eimer to destination folder
  def copy_eimer(self):
    # initial local variable
    eimer_path = self.entry_eimer.get()
    dest_path = self.entry_dest.get()
    eimer = var.get()
    filename = self.box.get()
  
    # check null eimer path : dialog warning
    if (len(eimer_path) == 0):
      #print ("put eimer path again")
      msgbox = Tk()
      msgbox.title("Warning")
      msgbox.geometry("130x40")
      label = Label(msgbox, text="Please put eimer path")
      label.grid()
      btn = Button(msgbox, text="OK", command=msgbox.destroy)
      btn.grid()
    # check exist eimer directory
    elif (os.path.isdir(eimer_path.replace("\\","//")) == False):
      msgbox3 = Tk()
      msgbox3.title("Warning")
      msgbox3.geometry("130x40")
      label3 = Label(msgbox3, text="Not found this eimer path")
      label3.grid()
      btn3 = Button(msgbox3, text="OK", command=msgbox3.destroy)
      btn3.grid()
    # check null destination path : dialog warning
    elif (len(dest_path) == 0):
      #print ("put destination path again")
      msgbox2 = Tk()
      msgbox2.title("Warning")
      msgbox2.geometry("130x40")
      label2 = Label(msgbox2, text="Please put destination path")
      label2.grid()
      btn2 = Button(msgbox2, text="OK", command=msgbox2.destroy)
      btn2.grid()
    # check exist destination directory
    elif (os.path.isdir(dest_path.replace("\\","//")) == False):
      msgbox4 = Tk()
      msgbox4.title("Warning")
      msgbox4.geometry("130x40")
      label4 = Label(msgbox4, text="Not found this destination path")
      label4.grid()
      btn4 = Button(msgbox4, text="OK", command=msgbox4.destroy)
      btn4.grid()
    # check select at Radiobutton
    elif (len(eimer) == 0):
      msgbox5 = Tk()
      msgbox5.title("Warning")
      msgbox5.geometry("130x40")
      label5 = Label(msgbox5, text="Please select eimer")
      label5.grid()
      btn5 = Button(msgbox5, text="OK", command=msgbox5.destroy)
      btn5.grid()
    # correct eimer and destination path
    else:
      # get file name and read file list from text file
      f = open(os.getcwd() + "\\filelist\\" + eimer + "\\" + filename + ".txt", "rb")
      f_read = f.read()
      f.close()
    
      # get eimer mc and copy source file
      f_list = f_read.strip().splitlines()
      not_found = str()
      cnt_all = 0
      cnt_copy = 0
      for i in f_list:
        srcfile = eimer_path + "\\eimer_" + eimer + "\\" + i.decode("utf-8")
        dstdir = dest_path + "\\" + i.decode("utf-8")
        #if not found some source file in eimer
        if (os.path.isfile(srcfile) == False):
          print("Cannot copy" + i.decode("utf-8"))
          not_found += i.decode("utf-8") + "\r\n"
        else:
          print(i.decode("utf-8"))
          shutil.copy(srcfile, dstdir)
          cnt_copy += 1
        cnt_all += 1
      
      #if not found file, report to user
      f_report = codecs.open("not_found_" + filename + "_" +eimer + ".txt", "wb", "utf-8")
      f_report.write("Cannot copy some file because not found in eimer path : ")
      f_report.write(eimer_path + "\r\n")
      f_report.write(not_found)
      f_report.close()
      
      # finish copy file
      msgbox6 = Tk()
      msgbox6.title("Complete")
      msgbox6.geometry("130x40")
      label6 = Label(msgbox6, text="Copy completed" + str(cnt_copy) + "/" + str(cnt_all))
      label6.grid()
      btn6 = Button(msgbox6, text="OK", command=msgbox6.destroy)
      btn6.grid()
      
      # copy eimer_path and dest_path to tmp file
      #f_config = open("config.txt", "wb")
      #f_config.write(eimer_path + "/n" + dest_path)
      #f_config.close()
      
    #print(eimer_path, dest_path, eimer, filename)
  

# for debug
if __name__=="__main__":

  # create windows
  root = Tk()
  # modified root windows
  root.title("Copy LE125 code")
  root.geometry("500x220")

  #initial global variable for Radiobutton
  var = StringVar()
  
  # add this to show content in GUI
  app = Application(root)

  # kick off the event loop
  root.mainloop()
  
