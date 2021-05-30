from Funciones.interfaz import InicioLinux, InicioWindows
import platform

# Constantes
SYSTEM = platform.system()


if __name__ == "__main__":
    if SYSTEM == 'Linux':
        InicioLinux()
    else:
        InicioWindows()