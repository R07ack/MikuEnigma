import random
from tkinter import *

c = 0

def continuar():
    global c
    c = c + 1
    print(c)


v = Tk()

v.title("MIKU ENIGMA")
v.geometry("1200x500")
v.resizable(1,1)
v.configure(background='#000000')


btnC = Button(v, text='Continuar', fg='black', bg='white', font=('Terminal', 18), command=continuar)
btnC.pack()

v.mainloop()