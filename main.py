from tkinter import *
from tkinter import messagebox
import platform
from Funciones.reconocimiento import reconocerRostro

# Variables
SYSTEM = platform.system()

ventana = Tk()
ventana.title("Reconocimiento de Gestos")


# Function to center window
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2 
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def other():
    ventana2 = Tk()
    ventana2.title("")
    ventana2.geometry("200x200")

    # Label
    label = Label(ventana2,text="Nombre")
    label.place(x=10,y=50)

    # Input
    input = Entry(ventana2)
    input.place(x=10, y=70)

    # Funtions
    def pasarNombre():
        name = input.get()
        #print(name)    

        ventana2.destroy()

        reconocerRostro(name)

    # Boton
    boton = Button(ventana2, text="Enviar", command=pasarNombre)
    boton.place(x=70,y=100)

    center(ventana2)
    ventana2.mainloop()


def WindowsSystem():
    if SYSTEM == 'Windows':
        ventana.attributes('')

        ventana.mainloop()


def LinuxSystem():
    if SYSTEM == 'Linux':
        ventana.attributes('-zoomed', True)

        boton = Button(ventana, text="Entrenamiento", font=('Arial',12), width=30, height=30, command=other)
        boton.place(x=30, y=50)

        ventana.mainloop()


if SYSTEM == 'Linux':
    LinuxSystem()
else:
    WindowsSystem()