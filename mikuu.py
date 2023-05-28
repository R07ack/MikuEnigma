import random
from tkinter import *

si_c = 0
sub_c = 0

r1 = random.randint(0,51)
print(r1)
r2 = 'PATOS'
r3 = 'SLAVERY'
r4 = 'NICONICOMUSICPARTY2015'
r5 = 'MIKUSIEMPREGANA15'

# Preguntas

# 1
r1_c = 0
limInf = 0
limSup = 50
t = 'el número está entre {} y {}.'
def p1():
    global r1_c
    r1_c = r1_c + 1
    if sub_c == 1:
        btnOK.pack_forget()
        entry.delete(0, END)
        entry.pack(pady = 10)
        btnSub.pack()
    elif r1_c > 0 and r1_c < 8:
        r = entry.get()
        entry.delete(0, END)
        if int(r) != r1:
            global limInf
            global limSup
            if int(r) > r1:
                limSup = int(r)
            else:
                limInf = int(r)
            if r1_c == 1:
                script.config(text='¡Incorrecto! Pero no te preocupes, ' + t.format(limInf, limSup))
            elif r1_c == 2:
                script.config(text='¡Vamos! No es tan difícil, ' + t.format(limInf, limSup))
            elif r1_c == 3:
                script.config(text='¡Tú puedes! ' + t.format(limInf, limSup).capitalize())
            elif r1_c == 4:
                script.config(text='...' + t.format(limInf, limSup))
            elif r1_c == 5:
                script.config(text='La respuesta es ' + str(r1) + '.')
            elif r1_c == 6:
                script.config(text='Solo coloca la respuesta...')
            elif r1_c == 7:
                script.config(text=str(r1) + '.')
                entry.pack_forget()
                btnSub.pack_forget()
                btnOK.pack()
        else: 
            script.config(text=' ¡Correcto! increíble, genial! Sigamos :)')
            entry.pack_forget()
            btnSub.pack_forget()
            btnOK.pack()



# Funciones

def opt():
    btnSI.pack(pady = 10)
    btnNO.place(x = 505, y = 360)


def entryy():
    entry.pack()
    btnSub.pack(pady=10)
    btnOK.pack_forget()


def click():
    text =texts.pop(0)
    script.config(text=text)
    if text == '¿Empezamos por tu nombre?':
        entryy()
    elif text == '¿Comprendes las reglas?':
        opt()
        btnOK.pack_forget()
    elif text == 'Primera pregunta: Estoy pensando en un número entre  0 y  50.  ¿Puedes adivinarlo?':
        p1()
        

def submit():
    global sub_c
    sub_c = sub_c + 1
    if sub_c == 1:
        nombre = entry.get()
        entry.pack_forget()
        btnSub.pack_forget()
        script.config(text='¡Hola, '+nombre+'!')
        btnOK.pack()
    else:
        p1()


def continuar():
    letter.destroy()
    btnC.destroy()
    script.pack(pady=100)
    btnOK.pack()


def si():
    global si_c
    si_c = si_c + 1
    if si_c == 1:
        qstn.destroy()
        btnSI.pack_forget()
        btnNO.place_forget()
        letter.pack(padx=10, pady=60)
        btnC.pack(padx=10, pady=20)
    if si_c == 2:
        script.config(text='Empecemos :)')
        btnSI.pack_forget()
        btnNO.place_forget()
        btnOK.pack()


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
           'Primera pregunta: Estoy pensando en un número entre  0 y  50.  ¿Puedes adivinarlo?', 
           'Siguiente pregunta: ¡Dicen por ahí que una imagen vale más que mil palabras!']

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
btnOK = Button(v, text='Ok', font=('Terminal', 18), bg='white', fg='black', command=click)
btnSub = Button(v, text='Submit', font=('Terminal', 18), bg='white', fg='black', command=submit)
entry = Entry(v, font=('Terminal', 20), bg='white', fg='black')

v.mainloop()