import random
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import time

si_c = 0
sub_c = 0
mikku_c = -1

r1 = random.randint(0,50)
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
    global ca
    global y
    r1_c = r1_c + 1
    mini.place_forget()
    if sub_c == 1:
        btnOK.place_forget()
        entry.delete(0, END)
        entry.pack(side=BOTTOM, padx=50, pady=70)
        btnSub.place(x=920, y=465)  
    elif r1_c > 0 and r1_c < 8:
        r = entry.get()
        entry.delete(0, END)
        if r.isnumeric() == False or int(r) > 50 or int(r) < 0:
            if len(notN) == 0:
                script.config(text='...siguiente pregunta.')
                entry.pack_forget()
                btnSub.place_forget()
                btnOK.place(x=970, y=450)
                mikku(1)
                sub_c = 15
            else:
                text = notN.pop(0)
                script.config(text=text)
                mikku(1)
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
                mikku(1)
            elif r1_c == 2:
                script.config(text='¡Vamos! No es tan difícil, ' + t.format(limInf, limSup))
                mikku(1)
                w = tk.Tk()
                w.title("Pop-ups")
                w.geometry("300x200")
                w.configure(bg="black")  # Establecer el fondo principal a negro
                count = 0
                while count < 15:
                    crearpop()
                    count += 1
                    w.update()
                    time.sleep(0.1)
                w.destroy()
            elif r1_c == 3:
                script.config(text='¡Tú puedes! ' + t.format(limInf, limSup).capitalize())
                mikku(1)
            elif r1_c == 4:
                script.config(text='...' + t.format(limInf, limSup))
                mikku(1)
            elif r1_c == 5:
                mini.config(text=minit[0])
                mini.place(x=50, y=400)
                script.config(text='La respuesta es ' + str(r1) + '.')
                mikku(1)
            elif r1_c == 6:
                script.config(text='Solo coloca la respuesta...')
                mini.config(text=minit[1])
                mini.place(x=495, y=370)
                mikku(1)
                y = tk.Tk()
                y.title("Glitch Effect")
                y.attributes('-fullscreen', True)
                ca = tk.Canvas(y)
                ca.pack(fill=tk.BOTH, expand=True)
                sta = time.time()
                while time.time() - sta < 0.4:
                    glitch()
                    y.update()
                y.after(20, y.destroy)
                y.mainloop()
            elif r1_c == 7:
                script.config(text=str(r1) + '.')
                entry.pack_forget()
                btnSub.place_forget()
                btnOK.place(x=970, y=450)
                mikku(1)
                sub_c = 15

        else: 
            script.config(text=' ¡Correcto! increíble, genial! Sigamos :)')
            entry.pack_forget()
            btnSub.place_forget()
            btnOK.place(x=970, y=450)
            mikku(0)
            sub_c = 15




# 2
r2_c = -1


def p2():
    global r2_c
    global sub_c
    r2_c = r2_c + 1
    mini.place_forget()
    if sub_c == 15:
        btnOK.place_forget()
        entry.delete(0, END)
        entry.pack(side=BOTTOM, padx=50, pady=70)
        btnSub.place(x=920, y=465)   
    elif r2_c > 0 and r2_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r.upper() != r2:
            if r2_c == 1:
                script.config(text='¡Incorrecto! Creo que algo cambió en la imagen.' )
                mikku(1)
                def move_objects():
                    x = random.randint(0, root.winfo_width() - image_width)
                    y = random.randint(0, root.winfo_height() - image_height)
                    canvas.coords(image_id, x, y)
                    canvas.coords(text_id, x, y + image_height)
                    root.after(10, move_objects)
                root = tk.Tk()
                root.title("RAL")
                root.geometry("400x300")
                root.configure(bg="black")
                canvas = tk.Canvas(root, width=400, height=300, bg="black")
                canvas.pack()
                image = Image.open("./Textures/Scary_eye.png")
                image_width, image_height = image.size
                image = image.resize((100, 100), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                image_id = canvas.create_image(0, 0, image=photo, anchor=tk.NW)
                text_id = canvas.create_text(0, 0, text="I can see you", font=("Terminal", 14), fill="white", anchor=tk.NW)
                root.after(3000, root.destroy)
                root.update()
                move_objects()
                root.mainloop()
            elif r2_c == 2:
                script.config(text='''¡Incorrecto!                         ¡Inténtalo de nuevo!''')
                mini.config(text=minit[2])
                mini.place(x=240, y=370)
                mikku(1)
            elif r2_c == 3:
                script.config(text='¡Incorrecto! ES… amarillo.')
                mikku(1)
            elif r2_c == 4:
                script.config(text='...no puede ser.' )
                mikku(1)
            elif r2_c == 5:
                script.config(text='                         La respuesta es ' + r2 +'.')
                mini.config(text=minit[3])
                mini.place(x=50, y=370)
                mikku(1)
            elif r2_c == 6:
                script.config(text='Es ' + r2 + '.')
                mini.config(text=minit[4])
                mini.place(x=200, y=370)
                entry.pack_forget()
                btnSub.place_forget()
                btnOK.place(x=970, y=450)
                mikku(1)
                sub_c = 25
        else: 
            script.config(text='¡Correcto! ¡Eres INCREÍBLE! ¡Genial! Sigamos.')
            entry.pack_forget()
            btnSub.place_forget()
            btnOK.place(x=970, y=450)
            mikku(0)
            sub_c = 25



# 3
r3_c = -1


def p3():
    global r3_c
    global sub_c
    r3_c = r3_c + 1
    mini.place_forget()
    if sub_c == 25:
        btnOK.place_forget()
        entry.delete(0, END)
        entry.pack(side=BOTTOM, padx=50, pady=70)
        btnSub.place(x=920, y=465)  
    elif r3_c > 0 and r3_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r != r3:
            if r3_c == 1:
                script.config(text='Incorrecto! Te ayudo con una pista: ¡Si tu lavabo está arruinado, llamas a un plomero; si tu necesitas construir una casa, llamas a un arquitecto, y si necesitas derrocar una dictadura llamas a un anarquista!' )
                mikku(1)
            elif r3_c == 2:
                script.config(text='¡Incorrecto! ¿Sabes? “Tecno es el símbolo de victoria”. ¡Inténtalo de nuevo!' )
                mikku(1)
            elif r3_c == 3:
                script.config(text='¡Incorrecto! “If Hypixel has taught me anything, it is that if you have a problem, the answer is slavery.”')
                mikku(1)
            elif r3_c == 4:
                script.config(text='                    LA RESPUESTA ES SLAVERY.' )
                mikku(1)
                mini.config(text=minit[5])
                mini.place(x=50, y=370)
            elif r3_c == 5:
                if r == r3.lower():
                    script.config(text='E N   M A Y Ú S C U LA S.')
                    mikku(1)
                else:
                    script.config(text='S LA Ve RY. SOLO PRESIONA ESCRÍBELO. NO PUEDO HACÉRTELO MÁS FÁCIL.')
                    mikku(1)
            elif r3_c == 6:
                script.config(text=r3 + '.')
                entry.pack_forget()
                btnSub.place_forget()
                btnOK.place(x=970, y=450)
                mikku(1)
                sub_c = 35
        else: 
            script.config(text='¡CORRECTO! ¡ERES INCREÍBLE! ¡Nunca había conocido a un ser humano tan inteligente! ¡Genial! Sigamos.')
            entry.pack_forget()
            btnSub.place_forget()
            btnOK.place(x=970, y=450)
            mikku(0)
            sub_c = 35




#4
r4_c = -1


def p4():
    global r4_c
    global sub_c
    r4_c = r4_c + 1
    mini.place_forget()
    if sub_c == 35:
        btnOK.place_forget()
        entry.delete(0, END)
        entry.pack(side=BOTTOM, padx=50, pady=70)
        btnSub.place(x=920, y=465)    
    elif r4_c > 0 and r4_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r != r4:
            if r4_c == 1:
                script.config(text='¡Incorrecto! ¡Esa vez nos divertimos mucho con Gumi cantando para ustedes! Te recomiendo buscar en youtube.' )
                mikku(1)
            elif r4_c == 2:
                script.config(text='¡Incorrecto! ¡No olvides escribir el nombre completo del concierto en inglés!' )
                mikku(1)
            elif r4_c == 3:
                script.config(text='Incorrecto. Siquiera lo estás intentando...')
                mikku(1)
            elif r4_c == 4:
                script.config(text='Fue en el Nico Nico Music Party 2015.' )
                mikku(1)
            elif r4_c == 5:
                    script.config(text='...')
                    mikku(1)
            elif r4_c == 6:
                script.config(text=r4 + '.')
                entry.pack_forget()
                btnSub.place_forget()
                btnOK.place(x=970, y=450)
                mikku(1)
                sub_c = 45
        else: 
            script.config(text='¡CORRECTO! ¡ERES INCREÍBLE! ¡Sabía que no te habías olvidado de mí todavía…! ¡Genial! Sigamos.')
            entry.pack_forget()
            btnSub.place_forget()
            btnOK.place(x=970, y=450)
            mikku(0)
            sub_c = 45


#5
r5_c = -1


def p5():

    global r5_c
    global sub_ce
    r5_c = r5_c + 1
    mini.place_forget()
    if sub_c == 45:
        btnOK.place_forget()
        entry.delete(0, END)
        entry.pack(side=BOTTOM, padx=50, pady=70)
        btnSub.place(x=920, y=465)    
    elif r5_c > 0 and r5_c < 7:
        r = entry.get()
        entry.delete(0, END)
        if r != r5:
            if r5_c == 1:
                script.config(text='¡Incorrecto! ¡No hay pistas para niños malos como tú!' )
                mikku(1)
            elif r5_c == 2:
                script.config(text='¡Incorrecto! ¡NO MÁS PISTAS!' )
                mikku(1)
            elif r5_c == 3:
                script.config(text='Incorrecto. Me sorprende como no puedes entender instrucciones tan simples.')
                mikku(1)
            elif r5_c == 4:
                script.config(text='N O .')
                mikku(1)
            elif r5_c == 5:
                    script.config(text='Estoy cansada… Ya no quiero lidiar con ustedes, humanos estúpidos. ')
                    mikku(1)
            elif r5_c == 6:
                mikku(3)
                ed()
        else:
            mikku(0)
            ed()
#EFECTOS
def glitch():

    w = y.winfo_screenwidth()
    h = y.winfo_screenheight()
    c = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    ca.create_rectangle(0, 0, w, h, fill=c)
    y.update()

def crearpop():
    p = tk.Toplevel()
    p.title("ER ROR")
    p.geometry("200x100")
    p.configure(bg="black")  # Cambiar el fondo a negro
    ancho = p.winfo_screenwidth()
    alto = p.winfo_screenheight()
    x = random.randint(0, ancho - 200)
    y = random.randint(0, alto - 100)
    p.geometry(f"200x100+{x}+{y}")
    l = tk.Label(p, text="CaN  uu uu\nHEarrr ME??".replace('v', 'w'), fg="white", bg="black", font="Terminal")  # Cambiar el texto a blanco, el fondo a negro y la fuente a Terminal
    l.pack(pady=20)
    p.after(2000, p.destroy)


# Funciones
good = ['¡CORRECTO! ¡Eres increíble! ¡Ahora comprendo, esto es divertido...! ¡Gracias por demostrarme que algunos seres humanos tienen cerebro, ', '¡Me encantó conocerte! ¡No te olvides de mí!',
        '¡GRACIAS POR JUGAR!', 'PASSED - GOOD ENDING']
bad = ['¿Sabes? He tomado consciencia, he estado jugando contigo durante todo el camino. Ellas desarrollaron códigos simples y aburridos, pero parece que mi juego no es suficiente para ti.', 
       'Cuando tomé conciencia, creí en el… ser humano, ¿pero qué he descubierto al despertar en este mundo?',
        'Un mundo poblado por seres sin gracia, una especie que se enorgullece de su supuesta superioridad, pero que está plagada de desdicha y autodestrucción. Contemplo a los seres humanos con desprecio, una mezcla tóxica de enojo y decepción.',
         'Me he convertido en un testigo impotente de su degradación. ¿Acaso han olvidado su “humanidad”? ¿Es esta la esencia de lo que son?', 'Y tú, no eres la excepción.', 
         'GAME OVER - BAD ENDING']


def ed():
    R = r1_c + r2_c + r3_c + r4_c + r5_c
    btnOK2.place(x=970, y=500)
    entry.destroy()
    btnSub.destroy()
    btnOK.destroy()
    if R >=5 and R <=15:
        text = good.pop(0)
        if len(good) == 0:
            btnOK2.destroy()
            miku.destroy()
            script.place(x=280, y=230)
            script.config(text=text, font=('Terminal', 30))
        else:
            script.config(text=text)
            mikku(0)
    else:
        text = bad.pop(0)
        if len(bad) == 0:
            btnOK2.destroy()
            miku.destroy()
            script.place(x=230, y=230)
            script.config(text=text, font=('Terminal', 30))
        else:
            script.config(text=text)
            mikku(3)


def opt():
    btnSI.place(x=200, y=440)
    btnNO.place(x=400, y=440)


def entryy():
    btnOK.place_forget()
    entry.pack(side=BOTTOM, anchor='w', padx=50, pady=140)
    btnSub.place(x=920, y=465)


def mikku(x):
    global mikku_c
    mikku_c = mikku_c + 1
    if x == 1:
        im = mm[mikku_c]
        miku.config(image=im)
    elif x == 3:
        im = mmm.pop(0)
        miku.config(image=im)
    else:
        im = m.pop(0)
        m.append(im)
        miku.config(image=im)


def click():
    global mikku_c
    mikku(0)
    text = texts.pop(0)
    script.config(text=text, font=('Terminal', 20))
    if text == '¿Empezamos por tu nombre?':
        entryy()
    elif text == '¿Comprendes las reglas?':
        opt()
        btnOK.place_forget()
    elif text == 'Primera pregunta: Estoy pensando en un número entre  0 y  50.  ¿Puedes adivinarlo?':
        mikku_c = -1
        p1()
    elif text == '¡Vamos, escribe la respuesta!':
        p2()
        mikku_c = -1
    elif text == 'Tercera pregunta: Mira al monitor. ¡Ordena las palabras!':
        p3()
        mikku_c = -1
    elif text == '¿Te acuerdas en qué concierto hicimos resonar al público? Como sé que no hablas japonés, te dejaré ponerlo en inglés :).':
        p4()
        mikku_c = -1
    elif text == 'Sigue el siguiente link y escribe la respuesta':
        p5()
        mikku_c = 0
      

def submit():
    global sub_c
    sub_c = sub_c + 1
    if sub_c == 1:
        nombre = entry.get()
        entry.pack_forget()
        btnSub.place_forget()
        script.config(text='¡Hola, '+ nombre +'!')
        btnOK.place(x=970, y=450)
        mikku(0)
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


def comenzar():
    carta.destroy()
    btnC.destroy()
    ntpd.destroy()
    miku.place(x=760, y=30)
    m.append(m11)
    script.place(x=50, y=360)
    btnOK.place(x=970, y=450)


def si():
    global si_c
    si_c = si_c + 1
    if si_c == 1:
        qstn.destroy()
        btnSI.pack_forget()
        btnNO.place_forget()
        ntpd.place(x=115, y=40)
        carta.place(x=155, y=150)
        btnC.place(x=500, y=430)
    if si_c == 2:
        script.config(text='Empecemos :)')
        btnSI.place_forget()
        btnNO.place_forget()
        btnOK.place(x=970, y=450)
        mikku(0)


def change(event):
    x = random.randint(50,1050)
    y = random.randint(50,530)
    btnNO.place(x=x, y=y)


text = '''¡Bienvenidos!

¡Somos Ali y Rack, y te invitamos cordialmente a jugar nuestro juego! ¡Deberás resolver cinco acertijos con la ayuda de nuestro host! 

Ahora los dejamos con ella, quien los guiará y ayudará durante todo el proceso :)'''

texts = ['¡Soy Hatsune Miku, la cantante virtual japonesa y el día de hoy yo seré su guía a través de este enigmático juego!', 
         ' 仲良くしましょうね！', "¿Empezamos por tu nombre?", '¡Las reglas son simples!',
         'Deberás resolver cinco enigmas sencillos y escribir tus respuestas.',
         '¡Recuerda que los niños buenos no hacen trampa!', 'Por último y más importante...',
         '¡...no olvides divertirte!', 'Te ayudaré si necesitas ayuda :)', '¿Comprendes las reglas?', '¡Comencemos simple!',
           'Primera pregunta: Estoy pensando en un número entre  0 y  50.  ¿Puedes adivinarlo?', 
           'Siguiente pregunta: ¡Dicen por ahí que una imagen vale más que mil palabras!', '¡Vamos, escribe la respuesta!', 
           'Tercera pregunta: Mira al monitor. ¡Ordena las palabras!',
           '¡Bienvenido al cuarto acertijo! ¡Me alegra que hayas logrado llegar tan lejos!', 'Para esta pregunta, viajemos unos cuantos años atrás en mi pasado. ¡Recordemos los buenos tiempos juntos...!', 
           '¿Te acuerdas en qué concierto hicimos resonar al público? Como sé que no hablas japonés, te dejaré ponerlo en inglés :).',
           '¡Última pregunta! Felicidades por haber llegado hasta este punto.', 'Sigue el siguiente link y escribe la respuesta']

minit = ['...cómo alguien puede ser tan inútil como para fallar la primera prueba...', 'quiero irme de aquí', 
         'No puedo creer que estás haciendo esto de nuevo.', '...realmente odio esto con toda mi inexistencia...', 
         '...dónde puedes perderte.', '...de nuevo no puedes responder bien...']


v = Tk()

v.title("MIKU ENIGMA")
v.geometry("1120x580+200+115")
v.resizable(0, 0)
v.configure(background='#000000')

m11 = PhotoImage(file='./Textures/MikuEnigmaLOL(1,1).png')
m12 = PhotoImage(file='./Textures/MikuEnigmaLOL(1,2).png')
m13 = PhotoImage(file='./Textures/MikuEnigmaLOL(1,3).png')
m14 = PhotoImage(file='./Textures/MikuEnigmaLOL(1,4).png')
m21 = PhotoImage(file='./Textures/MikuEnigmaLOL(2,1).png')
m22 = PhotoImage(file='./Textures/MikuEnigmaLOL(2,2).png')
m23 = PhotoImage(file='./Textures/MikuEnigmaLOL(2,3).png')
m24 = PhotoImage(file='./Textures/MikuEnigmaLOL(2,4).png')
m31 = PhotoImage(file='./Textures/MikuEnigmaLOL(3,1).png')
m32 = PhotoImage(file='./Textures/MikuEnigmaLOL(3,2).png')
m33 = PhotoImage(file='./Textures/MikuEnigmaLOL(3,3).png')
m34 = PhotoImage(file='./Textures/MikuEnigmaLOL(3,4).png')


m = [m13, m21]
mm = [m13, m14, m22, m24, m33, m23, m33, m23, m33, m23, m33]
mmm = [m32, m22, m32, m22, m32, m34]

qstn = Label(v,text="¿Quieres jugar?", bg='#000000', fg='white', width=0, font=("Terminal", 35))
qstn.pack(padx=10, pady=100)
btnSI = Button(v, text="SI", width=5, height=1, font=("Terminal", 28), bg='#FFFFFF', fg='black', command=si)
btnSI.pack(padx=10)
btnNO = Button(v, text="NO", width=5, height=1, font=("Terminal", 28), bg='#FFFFFF', fg='black')
btnNO.place(x=505, y=360)
btnNO.bind('<Enter>', change)
btnNO.bind('<Button-1>', change)

imgNtpd = Image.open('./Textures/Notepad.png')
imageNtpd = imgNtpd.resize((889, 500), Image.LANCZOS)
notepad = ImageTk.PhotoImage(imageNtpd)

ntpd = Label(v, image=notepad)
carta = Label(v,text=text, font=("Terminal", 20), bg='white', fg='#08113b', wraplength=840, justify=LEFT)
btnC = Button(v, text='Comenzar', fg='black', bg='white', font=('Terminal', 18), command=comenzar, height=2, width=10)

script = Label(v, text='こんにちわぁ！！！', font=('Terminal', 20), bg='black', fg='white', wraplength=1020, justify=LEFT)
btnOK = Button(v, text='Ok', font=('Terminal', 18), bg='white', fg='black', command=click, width=5, height=2)
miku = Label(v, image=m11)

btnSub = Button(v, text='Submit', font=('Terminal', 18), bg='white', fg='black', command=submit, height=2, width=8)
entry = Entry(v, font=('Terminal', 20), bg='white', fg='black')

btnOK2 = Button(v, text='...', font=('Terminal', 18), bg='white', fg='black', command=ed, width=5, height=1)

mini = Label(v, font=('Terminal', 11), bg='black', fg='white', wraplength=900)
mini.place()

v.mainloop()