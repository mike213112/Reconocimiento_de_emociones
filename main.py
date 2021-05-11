from tkinter import *
from tkinter import messagebox
import platform
from Database.database import *

SYSTEM = platform.system()

windows = Tk()
windows.title('Deteccion de Emociones')

"""
    funtion for detect system
"""
def WindowsPlatform(system):
    if system == 'Windows':
        windows.attributes('-fullscreen', True)


def LinuxPlatform(system):
    if SYSTEM == 'Linux':
        windows.attributes('-zoomed', True)

        add_photo('hola')

        windows.mainloop()


#WindowsPlatform(SYSTEM)
LinuxPlatform(SYSTEM)