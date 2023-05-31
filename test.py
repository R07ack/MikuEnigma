import tkinter as tk
import random
import time

def crearpop():
    p = tk.Toplevel()
    p.title("ER ROR")
    p.geometry("200x100")
    ancho = p.winfo_screenwidth()
    alto = p.winfo_screenheight()
    x = random.randint(0, ancho - 200)
    y = random.randint(0, alto - 100)
    p.geometry(f"200x100+{x}+{y}")
    l = tk.Label(p, text="Ca N  uu uu HEarrr ME??")
    l.pack(pady=20)
    p.after(2000, p.destroy)

v = tk.Tk()
v.title("Pop-ups")
v.geometry("300x200")

count = 0

while count < 15:
    crearpop()
    count += 1
    v.update()
    time.sleep(0.1)

v.mainloop()
#-------------------------------------------------------------------------------------
def glitch():
    w = v.winfo_screenwidth()
    h = v.winfo_screenheight()
    c = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    ca.create_rectangle(0, 0, w, h, fill=c)
    v.update()
v = tk.Tk()
v.title("Glitch Effect")
v.attributes('-fullscreen', True)
ca = tk.Canvas(v)
ca.pack(fill=tk.BOTH, expand=True)
sta = time.time()
while time.time() - sta < 0.4:
    glitch()
    v.update()
v.after(20, v.destroy)
v.mainloop()
