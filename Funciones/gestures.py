from reconocimiento import facesuser
from getpass import getuser


def reconocerRostro(nombre):
    if nombre == "":
        name = getuser()    
        facesuser(name)
    else:
        facesuser(nombre)


def Desprecio():
    nombre_de_la_emocion = 'desprecio'
    facesuser(nombre_de_la_emocion)


def Tristeza():
    nombre_de_la_emocion = 'tristeza'
    facesuser(nombre_de_la_emocion)


def Sorpresa():
    nombre_de_la_emocion = 'sorpresa'
    facesuser(nombre_de_la_emocion)


def Miedo():
    nombre_de_la_emocion = 'Asco'
    facesuser(nombre_de_la_emocion)


def Felicidad():
    nombre_de_la_emocion = 'felicidad'
    facesuser(nombre_de_la_emocion)


def Enfado():
    nombre_de_la_emocion = 'enojo'
    facesuser(nombre_de_la_emocion)
