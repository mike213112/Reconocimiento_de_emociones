import cv2
import os
import numpy as np


def faceip():
    path = os.getcwd() + '/Fotos'

    listar = os.listdir(path)
    print('lista personas', listar)

    for names in listar:
        personpath = path + '/' + names
        print('Leyendo imagenes')

        for filename in os.listdir(personpath):
            print('imagen: ', names + '/' + filename)