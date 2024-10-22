import os
import subprocess

#ruta prueba
#C:\Users\Ismael\ISMAEL_CICLO_SUPERIOR\SEGUNDO DAM\PSP\archivos\2.txt
# Solicitar la ruta del archivo al usuario
file_path = input("Introduce la ruta del archivo que deseas abrir: ")

# Abrir el archivo con Notepad, indicamos el programa con el que lo vamos abrir
subprocess.run(['notepad.exe', file_path])



