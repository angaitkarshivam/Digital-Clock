from tkinter import *
from time import strftime

window = Tk()
window.title ("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    Lbl.config(text=string)
    Lbl.after(1000, time)

Lbl = Label(window, font =('arial', 160, 'bold'), bg='black', fg='white')
Lbl.pack(anchor='center', fill ='both', expand=1)

time()
window.mainloop()
