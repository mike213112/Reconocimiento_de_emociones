from tkinter import *
from tkinter import messagebox
import platform
from Database.database import *
import cv2
import os
import imutils

SYSTEM = platform.system()

windows = Tk()
windows.title('Deteccion de Emociones')

CARPETAFELICIDAD = os.mkdir(mostrar + "/Fotos/Felicidad")
CARPETAENOJO = os.mkdir(mostrar + "/Fotos/Enojo")
CARPETAMIEDO = os.mkdir(mostrar + "/Fotos/Miedo")
CARPETATRISTEZA = os.mkdir(mostrar + "/Fotos/Tristeza")
CARPETASORPRESA = os.mkdir(mostrar + "/Fotos/Sorpresa")
CARPETAASCO = os.mkdir(mostrar + "/Fotos/Asco")

"""
    Funcion de entramiento
"""
def entramiento():
    pass

"""
    funtion for detect system
"""
def WindowsPlatform(system):
    if system == 'Windows':
        windows.attributes('-fullscreen', True)
        windows.mainloop()

def LinuxPlatform(system):
    if SYSTEM == 'Linux':
        windows.attributes('-zoomed', True)

        boton = Button(windows, text="Entrenamiendo de la IA", font=('Arial',18),fg="red")
        boton.place(x=50, y=100)

        windows.mainloop()


#WindowsPlatform(SYSTEM)
LinuxPlatform(SYSTEM)
mostrar = os.getcwd()
