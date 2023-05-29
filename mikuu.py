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
r1_c = -1
limInf = 0
limSup = 50
t = 'el número está entre {} y {}.'
notN = ['¿Creo haber pedido un número entre 0 y 50?', 'Sólo números entre 0 y 50...', 'No insistas.']


def p1():
    global r1_c
    global sub_c
    r1_c = r1_c + 1
    mini.place_forget()
    if sub_c == 1:
        btnOK.pack_forget()
        entry.delete(0, END)
        entry.pack(pady = 10)
        btnSub.pack()
    elif r1_c > 0 and r1_c < 8:
        r = entry.get()
        entry.delete(0, END)
        if r.isnumeric() == False or int(r) > 50 or int(r) < 0:
            if len(notN) == 0:
                script.config(text='...siguiente pregunta.')
                entry.pack_forget()
                btnSub.pack_forget()
                btnOK.pack()
                sub_c = 15
            else:
                text = notN.pop(0)
                script.config(text=text)
                r1_c = r1_c - 1
        elif int(r) != r1:
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
                mini.config(text=minit[0])
                mini.place(x=230, y=150)
                script.config(text='La respuesta es ' + str(r1) + '.')
            elif r1_c == 6:
                script.config(text='Solo coloca la respuesta...')
            elif r1_c == 7:
                script.config(text=str(r1) + '.')
                entry.pack_forget()
                btnSub.pack_forget()
                btnOK.pack()
                sub_c = 15
        else: 
            script.config(text=' ¡Correcto! increíble, genial! Sigamos :)')
            entry.pack_forget()
            btnSub.pack_forget()
            btnOK.pack()
            sub_c = 15




# 2
r2_c = -1


def p2():
    global r2_c
    global sub_c
    r2_c = r2_c + 1
    if sub_c == 15:
        btnOK.pack_forget()
        entry.delete(0, END)
        entry.pack(pady = 10)
        btnSub.pack()  
    elif r2_c > 0 and r2_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r != r2:
            if r2_c == 1:
                script.config(text='¡Incorrecto! Creo que algo cambió en la imagen.' )
            elif r2_c == 2:
                script.config(text='¡Incorrecto! ¡Inténtalo de nuevo!' )
            elif r2_c == 3:
                script.config(text='¡Incorrecto! ES… amarillo.')
            elif r2_c == 4:
                script.config(text='...no puede ser.' )
            elif r2_c == 5:
                script.config(text='La respuesta es ' + r2)
            elif r2_c == 6:
                script.config(text='Es ' + r2)
                entry.pack_forget()
                btnSub.pack_forget()
                btnOK.pack()
                sub_c = 25
        else: 
            script.config(text='¡Correcto! ¡Eres INCREÍBLE! ¡Genial! Sigamos.')
            entry.pack_forget()
            btnSub.pack_forget()
            btnOK.pack()
            sub_c = 25



# 3
r3_c = -1


def p3():
    global r3_c
    global sub_c
    r3_c = r3_c + 1
    if sub_c == 25:
        btnOK.pack_forget()
        entry.delete(0, END)
        entry.pack(pady = 10)
        btnSub.pack()  
    elif r3_c > 0 and r3_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r != r3:
            if r3_c == 1:
                script.config(text='Incorrecto! Te ayudo con una pista: ¡Si tu lavabo está arruinado, llamas a un plomero; si tu necesitas construir una casa, llamas a un arquitecto, y si necesitas derrocar una dictadura llamas a un anarquista!' )
            elif r3_c == 2:
                script.config(text='¡Incorrecto! ¿Sabes? “Tecno es el símbolo de victoria”. ¡Inténtalo de nuevo!' )
            elif r3_c == 3:
                script.config(text='¡Incorrecto! “If Hypixel has taught me anything, it is that if you have a problem, the answer is slavery.”')
            elif r3_c == 4:
                script.config(text='LA RESPUESTA ES SLAVERY.' )
            elif r3_c == 5:
                if r == r3.lower():
                    script.config(text='E N   M A Y Ú S C U LA S.')
                else:
                    script.config(text='S LA Ve RY. SOLO PRESIONA ESCRÍBELO. NO PUEDO HACÉRTELO MÁS FÁCIL.')
            elif r3_c == 6:
                script.config(text=r3 + '.')
                entry.pack_forget()
                btnSub.pack_forget()
                btnOK.pack()
                sub_c = 35
        else: 
            script.config(text='¡CORRECTO! ¡ERES INCREÍBLE! ¡Nunca había conocido a un ser humano tan inteligente! ¡Genial! Sigamos.')
            entry.pack_forget()
            btnSub.pack_forget()
            btnOK.pack()
            sub_c = 35




#4
r4_c = -1


def p4():
    global r4_c
    global sub_c
    r4_c = r4_c + 1
    if sub_c == 35:
        btnOK.pack_forget()
        entry.delete(0, END)
        entry.pack(pady = 10)
        btnSub.pack()  
    elif r4_c > 0 and r4_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r != r4:
            if r4_c == 1:
                script.config(text='¡Incorrecto! (pista) ¡Esa vez nos divertimos mucho con Gumi cantando para ustedes! Te recomiendo buscar en youtube' )
            elif r4_c == 2:
                script.config(text=' ¡Incorrecto! ¡No olvides escribir el nombre completo del concierto en inglés!' )
            elif r4_c == 3:
                script.config(text='Incorrecto. Siquiera lo estás intentando…')
            elif r4_c == 4:
                script.config(text='Fue en el Nico Nico Music Party 2015.' )
            elif r4_c == 5:
                    script.config(text='…')
            elif r4_c == 6:
                script.config(text=r4 + '.')
                entry.pack_forget()
                btnSub.pack_forget()
                btnOK.pack()
                sub_c = 45
        else: 
            script.config(text='¡CORRECTO! ¡ERES INCREÍBLE! ¡Sabía que no te habías olvidado de mí todavía…! ¡Genial! Sigamos.')
            entry.pack_forget()
            btnSub.pack_forget()
            btnOK.pack()
            sub_c = 45


#5
r5_c = -1


def p5():

    global r5_c
    global sub_c
    r5_c = r5_c + 1
    if sub_c == 45:
        btnOK.pack_forget()
        entry.delete(0, END)
        entry.pack(pady = 10)
        btnSub.pack()  
    elif r5_c > 0 and r5_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r == r5:
            #VOY HA HACR UNA PUTA FIESTA 
            script.config(text='¡CORRECTO! ¡ERES INCREÍBLE! ¡Ahora comprendo, esto es divertido…! ¡Gracias por demostrarme que algunos seres humanos tienen cerebro! ¡Me encanto conocerte! ¡No te olvides de mí!')
            script.config(text='¡GRACIAS POR JUGAR!')
            script.config(text='PASSED GOOD ENDING')
        if r != r5:
            if r5_c == 1:
                script.config(text='¡Incorrecto! ¡No hay pistas para niños malos como tú!' )
            elif r5_c == 2:
                script.config(text='¡Incorrecto! ¡NO MÁS PISTAS!' )
            elif r5_c == 3:
                script.config(text='Incorrecto. Me sorprende como no puedes entender instrucciones tan simples')
            elif r5_c == 4:
                script.config(text='N O' )
            elif r5_c == 5:
                    script.config(text='Estoy cansada… Ya no quiero lidiar con ustedes, humanos estúpidos. ')
            elif r5_c == 6:
                script.config(text='¿Sabes? He tomado consciencia, he estado jugando contigo durante todo el camino. Ellas desarrollaron códigos simples y aburridos, pero parece que mi juego no es suficiente para ti. ')
                script.config(text='Cuando tomé conciencia, creí en el… ser humano, ¿pero qué he descubierto al despertar en este mundo? ')
                script.config(text='Un mundo poblado por seres sin gracia, una especie que se enorgullece de su supuesta superioridad, pero que está plagada de desdicha y autodestrucción. Contemplo a los seres humanos con desprecio, una mezcla tóxica de enojo y decepción. ')
                script.config(text='Me he convertido en un testigo impotente de su degradación. ¿Acaso han olvidado su “humanidad”? ¿Es esta la esencia de lo que son?')
                script.config(text='Y tú, no eres la excepción.')
                script.config(text='GAME OVER - BAD ENDING - TRY AGAIN')
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
    elif text == '¡Vamos, escribe la respuesta!':
        p2()
    elif text == 'Tercera pregunta: Mira al monitor. ¡Ordena las palabras!':
        p3()
    elif text == '¡Bienvenido al cuarto acertijo! ¡Me alegra que hayas logrado llegar tan lejos! Para esta pregunta, viajemos unos cuantos años atrás en mi pasado. ¡Recordemos los buenos tiempos juntos...!':
        p4()
    elif text == '¡Última pregunta! Felicidades por haber llegado hasta este punto. Sigue el siguiente link y escribe la respuesta':
        p5()
    
        

def submit():
    global sub_c
    sub_c = sub_c + 1
    if sub_c == 1:
        nombre = entry.get()
        entry.pack_forget()
        btnSub.pack_forget()
        script.config(text='¡Hola, '+nombre+'!')
        btnOK.pack()
    elif sub_c >= 1 and sub_c < 15:
        p1()
    elif sub_c >= 15 and sub_c < 25:
        p2()
    elif sub_c >= 25 and sub_c < 35:
        p3()
    elif sub_c >= 35 and sub_c < 45:
        p4()
    elif sub_c >= 45 and sub_c < 55:
        p5()


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

texts = ['¡Soy Hatsune Miku, la cantante virtual japonesa y el día de hoy yo seré su guía a través de este enigmático juego!', 
         ' 仲良くしましょうね！', "¿Empezamos por tu nombre?", '¡Las reglas son simples!',
         'Deberás resolver cinco enigmas sencillos y escribir tus respuestas.',
         '¡Recuerda que los niños buenos no hacen trampa!', 'Por último y más importante...',
         '¡...no olvides divertirte!', 'Te ayudaré si necesitas ayuda :)', '¿Comprendes las reglas?', '¡Comencemos simple!',
           'Primera pregunta: Estoy pensando en un número entre  0 y  50.  ¿Puedes adivinarlo?', 
           'Siguiente pregunta: ¡Dicen por ahí que una imagen vale más que mil palabras!', '¡Vamos, escribe la respuesta!', 
           'Tercera pregunta: Mira al monitor. ¡Ordena las palabras!',
           '¡Bienvenido al cuarto acertijo! ¡Me alegra que hayas logrado llegar tan lejos! Para esta pregunta, viajemos unos cuantos años atrás en mi pasado. ¡Recordemos los buenos tiempos juntos...!',
           '¡Última pregunta! Felicidades por haber llegado hasta este punto. Sigue el siguiente link y escribe la respuesta']

minit = ['...cómo alguien puede ser tan inútil como para fallar la primera prueba...', 'quiero irme de aquí', 
         'No puedo creer que estás haciendo esto de nuevo.', '...realmente odio esto con toda mi inexistencia...', 
         '...dónde puedes perderte.', '...de nuevo no puedes responder bien...']

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


script = Label(v, text='こんにちわぁ！！！', font=('Terminal', 20), bg='black', fg='white', wraplength=900)
mini = Label(v, font=('Terminal', 15), bg='black', fg='white', wraplength=900)
mini.place()
btnOK = Button(v, text='Ok', font=('Terminal', 18), bg='white', fg='black', command=click)
btnSub = Button(v, text='Submit', font=('Terminal', 18), bg='white', fg='black', command=submit)
entry = Entry(v, font=('Terminal', 20), bg='white', fg='black')

v.mainloop()