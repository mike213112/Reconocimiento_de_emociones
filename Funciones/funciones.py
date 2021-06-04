from tkinter import *
from getpass import getuser
import platform
import cv2
import os
import imutils
import numpy as np


# Constantes
SYSTEM = platform.system()

""" Funcion para la captura de Rostros """
def facesuser(name):
    path = os.getcwd() + '/Fotos'

    namepath = path + '/' + name

    if not os.path.exists(namepath):
        os.makedirs(namepath)

    cap = cv2.VideoCapture(0)

    faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    contador = 0

    while True:
        ret, frame = cap.read()
        if ret == False:
            break

        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        face = faces.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h + 40), (0, 255, 0), 2)
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(namepath + '/{}_{}.png'.format(name, contador), rostro)
            contador = contador + 1
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == 27 or contador >= 300:
            break

    cap.release() 
    cv2.destroyAllWindows()


def reconocerRostro(nombre):
    if nombre == "":
        name = getuser()
        facesuser(name)
    else:
        facesuser(nombre)



""" Funciones para Entrenar """
def Entrenando():
    path = os.getcwd() + '/Fotos'
    #path = '/home/mike/Desktop/UMG/IA/Reconocimiento_de_emociones' + '/Fotos'
    listar_persona = os.listdir(path)

    labels = []
    datos_rostro = []
    label = 0

    for nombre_directorio in listar_persona:
        persona_path = path  + '/' + nombre_directorio

        for nombre_archivo in os.listdir(persona_path):
            print('Rostro: ', nombre_directorio + '/' + nombre_archivo)
            labels.append(label)
            datos_rostro.append(cv2.imread(persona_path + '/' + nombre_archivo, 0))
            """fotos = cv2.imread(persona_path + '/' + nombre_archivo, 0)
            cv2.imshow('fotos', fotos)
            cv2.waitKey(10)"""
        label = label + 1

    reconocer_rostro = cv2.face.EigenFaceRecognizer_create()
    #print('Entrenando ...')
    reconocer_rostro.train(datos_rostro, np.array(labels))

    #Almacenar
    #reconocer_rostro.write('modeloEigenFace.xml')
    #reconocer_rostro.write('modeloFisherFace.xml')
    reconocer_rostro.write('modeloLBPHFace.xml')
    #print('Modelo Almacenado')


def reconocimientoFacial():
    datapath = os.getcwd() + '/Fotos'
    #datapath = '/home/mike/Desktop/UMG/IA/Reconocimiento_de_emociones/Fotos'
    imagespath = os.listdir(datapath)
    print('images: ', imagespath)

    #reconocer_rostro = cv2.face.EigenFaceRecognizer_create()
    #reconocer_rostro = cv2.face.FisherFaceRecognizer_create()
    reconocer_rostro = cv2.face.LBPHFaceRecognizer_create()

    #reconocer_rostro.read('modeloEigenFace.xml')
    #reconocer_rostro.read('modeloFisherFace.xml')
    reconocer_rostro.read('modeloLBPHFace.xml')

    cap = cv2.VideoCapture(0)

    clasificar_rostro = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()

        if  ret == False:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = clasificar_rostro.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            result = reconocer_rostro.predict(rostro)

            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(0,255,0),1,cv2.LINE_AA)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #if result[0] < 7600:
            if result[1] < 4100:
                cv2.putText(frame,'{}'.format(imagespath[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h+40),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h+40),(0,255,0),2)

        cv2.imshow('frame',frame)

        k = cv2.waitKey(1)

        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


#facesuser('Miguel')
#Entrenando()
#reconocimientoFacial()

""" Emociones """
def Desprecio():
    nombre_de_la_emocion = 'desprecio'
    facesuser(nombre_de_la_emocion)
    Entrenando()


def Tristeza():
    nombre_de_la_emocion = 'tristeza'
    facesuser(nombre_de_la_emocion)
    Entrenando()


def Sorpresa():
    nombre_de_la_emocion = 'sorpresa'
    facesuser(nombre_de_la_emocion)
    Entrenando()


def Miedo():
    nombre_de_la_emocion = 'miedo'
    facesuser(nombre_de_la_emocion)
    Entrenando()


def Felicidad():
    nombre_de_la_emocion = 'felicidad'
    facesuser(nombre_de_la_emocion)
    Entrenando()


def Enfado():
    nombre_de_la_emocion = 'enojo'
    facesuser(nombre_de_la_emocion)
    Entrenando()


""" Funciones para la interfaz """
# Function to center window
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def Entrenamiento():
    entrenamiento = Tk()
    entrenamiento.title('Entrenamiento')
    entrenamiento.geometry('720x600')

    # Label
    label = Label(entrenamiento, text="Nombre")
    label.place(x=10, y=10)

    # Input
    campo = Entry(entrenamiento)
    campo.place(x=10, y=40)

    # Funtions
    """def pasarNombre():
        name = campo.get()

        entrenamiento.destroy()

        reconocerRostro(name)

    # Boton
    boton = Button(entrenamiento, text="Enviar", command=pasarNombre, bg='#154D04', fg='#FFFFFF')
    boton.place(x=120, y=65)"""

    def Enojo():
        Enfado()
        entrenamiento.destroy()


    def Feliz():
        Felicidad()
        entrenamiento.destroy()


    def Sorprendido():
        Sorpresa()
        entrenamiento.destroy()


    def Triste():
        Tristeza()
        entrenamiento.destroy()


    boton_enojo = Button(entrenamiento, text="Enojo", command=Enojo, bg='#154D04', fg='#FFFFFF', width=20, height=35)
    boton_enojo.place(x=0, y=0)

    boton_felicidad = Button(entrenamiento, text='Felicidad', command=Feliz, bg='#154D04', fg='#FFFFFF', width=20, height=35)
    boton_felicidad.place(x=180,y=0)
    
    boton_sorpresa = Button(entrenamiento, text='Sorpresa', command=Sorprendido, bg='#154D04', fg='#FFFFFF', width=20, height=35)
    boton_sorpresa.place(x=360, y=0)
    
    boton_tristeza = Button(entrenamiento, text='Tristeza', command=Triste, bg='#154D04', fg='#FFFFFF', width=20, height=35)
    boton_tristeza.place(x=540, y=0)

    center(entrenamiento)
    entrenamiento.mainloop()


def Emociones():
    emociones = Tk()
    emociones.title('Emociones')
    emociones.geometry('900x600')

    #boton_Enojo


    center(emociones)
    emociones.mainloop()


def InicioLinux():
    inicio = Tk()
    inicio.title('Inicio de Sesion')
    inicio.attributes('-zoomed', True)

    boton_entrenamiento = Button(inicio, text='Entrenamiento', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30, command=Entrenamiento)
    boton_entrenamiento.place(x=0, y=40)

    boton_emocion = Button(inicio, text='Emociones', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30, command=Emociones)
    boton_emocion.place(x=330, y=40)

    """boton_mascara = Button(inicio, text='Mascarilla', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30)
    boton_mascara.place(x=660, y=40)

    boton_lapiz = Button(inicio, text='Mascarilla', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30)
    boton_lapiz.place(x=990, y=40)"""

    inicio.config(background='gray')
    inicio.mainloop()


def InicioWindows():
    inicio = Tk()
    inicio.title('Inicio de Sesion')
    inicio.attributes('-fullscreen', True)

    boton_entrenamiento = Button(inicio, text='Entrenamiento', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30)
    boton_entrenamiento.place(x=0, y=40)

    boton_emocion = Button(inicio, text='Emociones', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30)
    boton_emocion.place(x=330, y=40)

    """boton_mascara = Button(inicio, text='Mascarilla', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30)
    boton_mascara.place(x=660, y=40)

    boton_lapiz = Button(inicio, text='Mascarilla', bg='#454545', fg='white', font=('Arial', 14), width=30, height=30)
    boton_lapiz.place(x=990, y=40)"""

    inicio.config(background='gray')
    inicio.mainloop()