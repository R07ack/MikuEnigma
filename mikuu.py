import random
from tkinter import *

global si_c
global sub_c

si_c = 0
sub_c = 0

r1 = random.randint(0,51)
r2 = 'PATOS'
r3 = 'SLAVERY'
r4 = 'NICONICOMUSICPARTY2015'
r5 = 'MIKUSIEMPREGANA15'

def r1():
    entry.delete(0, END)
    entry.pack(padx = 10)
    for i in range (5):
        print('lol')

def si1():
    script.config(text='Empecemos :)')
    btnSI.pack_forget()
    btnNO.place_forget()
    btn1.pack()

def opt():
    btnSI.pack(pady=10)
    btnNO.place(x=545,y=330)

def entry1():
    entry.pack()
    btn2.pack(pady=10)
    btn1.pack_forget()

def click():
    text =texts.pop(0)
    script.config(text=text)
    if text == '¿Empezamos por tu nombre?':
        entry1()
    elif text == '¿Comprendes las reglas?':
        opt()
        btn1.pack_forget()
        btnSI.config(command=si1)
    elif text == 'Primera pregunta: Estoy pensando en un número entre  0 y  50.  ¿Puedes adivinarlo?':
        r1()
        

def submit():
    global nombre
    nombre = entry.get()
    entry.pack_forget()
    btn2.pack_forget()
    script.config(text='¡Hola, '+nombre+'!')
    btn1.pack()

def continuar():
    letter.destroy()
    btnC.destroy()
    script.pack(pady=100)
    btn1.pack()

def si():
    
    qstn.destroy()
    btnSI.pack_forget()
    btnNO.place_forget()
    letter.pack(padx=10, pady=60)
    btnC.pack(padx=10, pady=20)

def change(event):
    x = random.randint(1,1150)
    y = random.randint(50,450)
    btnNO.place(x=x, y=y)

text = '''¡Bienvenidos! 

¡Somos Ali y Rack, y te invitamos cordialmente a jugar nuestro juego! 
¡Deberás resolver cinco acertijos con la ayuda de nuestro host! Ahora 
los dejamos con ella, quien los guiará y ayudará durante todo el 
proceso :)'''

texts = ['''¡Soy Hatsune Miku, la cantante virtual japonesa y
 el día de hoy yo seré su guía a través de este enigmático juego!''', ' 仲良くしましょうね！',
         "¿Empezamos por tu nombre?", '¡Las reglas son simples!',
         'Deberás resolver cinco enigmas sencillos y escribir tus respuestas.',
         '¡Recuerda que los niños buenos no hacen trampa!', 'Por último y más importante...',
         '¡...no olvides divertirte!', 'Te ayudaré si necesitas ayuda :)', '¿Comprendes las reglas?', '¡Comencemos simple!',
           'Primera pregunta: Estoy pensando en un número entre  0 y  50.  ¿Puedes adivinarlo?']

v = Tk()

v.title("MIKU ENIGMA")
v.geometry("1120x580")
v.resizable(1,1)
v.configure(background='#000000')

qstn = Label(v,text="¿Quieres jugar?", bg='#000000', fg='white', width=0, font=("Terminal", 35))
qstn.pack(padx=10, pady=100)
btnSI = Button(v, text="SI", width=5, height=1, font=("Terminal", 28), bg='#FFFFFF', fg='black', command=si)
btnSI.pack(padx=10)
btnNO = Button(v, text="NO", width=5, height=1, font=("Terminal", 28), bg='#FFFFFF', fg='black')
btnNO.place(x=505, y=360)
btnNO.bind('<Enter>', change)
btnNO.bind('<Button-1>', change)

letter = Label(v,text=text, font=("Terminal", 20), bg='black', fg='white')
btnC = Button(v, text='Continuar', fg='black', bg='white', font=('Terminal', 18), command=continuar)


script =Label(v, text='こんにちわぁ！！！', font=('Terminal', 20), bg='black', fg='white')
btn1 = Button(v, text='Ok', font=('Terminal', 18), command=click, bg='white', fg='black')
btn2 = Button(v, text='Submit', font=('Terminal', 18), command=submit, bg='white', fg='black')
entry = Entry(v, font=('Terminal', 20), bg='white', fg='black')

v.mainloop()