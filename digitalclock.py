from tkinter import *                                              # importing whole module
from tkinter.ttk import *

from time import strftime


root = Tk()                                                        # creating tkinter window
root.title(' Digital Clock ')

def time():
    string = strftime('%I : %M : %S %p')                           # 12-hour clock format
    lbl.config(text = string)
    lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('agency fb',150, 'bold'),background = 'black',foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()
