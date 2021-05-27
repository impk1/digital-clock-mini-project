#importing modules
from tkinter import *
from tkinter.ttk import *
#importing strftime function to retrieve system's time 
from time import strftime

#creating tkinter window
root = Tk()
root.configure(background="skyblue")
root.title("Clock")
root.resizable(False,False)
#styling the digital clock
clock_label = Label(root, font="calibri 40 bold" , foreground = "yellow")
clock_label.pack( anchor = "center")
#make function to display the time in label
def time():
    current_time = strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    clock_label.after(1000,time)
time()

mainloop()
