from Funciones.funciones import InicioLinux, InicioWindows
import platform
import os

# Constantes
SYSTEM = platform.system()

if __name__ == "__main__":
    if SYSTEM == 'Linux':
        path = os.getcwd()

        namepath = path + '/Fotos'

        if not os.path.exists(namepath):
            os.makedirs(namepath)
            InicioLinux()
    else:
        InicioWindows()