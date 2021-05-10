from tkinter import *
from tkinter import messagebox
import platform
from Database/config import config

config.connector

SYSTEM = platform.system()

windows = Tk()
windows.title('Deteccion de Emociones')

def WindowsPlatform(system):
    if system == 'Windows':
        windows.attributes('-fullscreen', True)


def LinuxPlatform(system):
    if SYSTEM == 'Linux':
        windows.attributes('-zoomed', True)
        windows.mainloop()


WindowsPlatform(SYSTEM)
LinuxPlatform(SYSTEM)
