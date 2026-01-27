import sys
import os


def obtener_ruta_base():
    """
    Devuelve la carpeta donde está el ejecutable o el script.
    Funciona para Python normal y para PyInstaller (--onefile).
    """
    if getattr(sys, 'frozen', False):
        # Ejecutable (.exe)
        return os.path.dirname(sys.executable)
    else:
        # Script .py
        return os.path.dirname(os.path.abspath(__file__))
