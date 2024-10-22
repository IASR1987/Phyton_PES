import os
import subprocess

#si introducimos la direccion de manera manual debemos ponerle r delante para que entienda que es una ruta
#cruda y no un string, ya que esto último da error
file_path=r"C:\Users\Ismael\ISMAEL_CICLO_SUPERIOR\SEGUNDO DAM\PSP\teoria Phyton\SHELL.subprocces.pdf"
#
# Abrir el archivo con su programa predeterminado
os.startfile(file_path)

# Solicitar la ruta del archivo al usuario
#file_path = input("Introduce la ruta del archivo que deseas abrir: ")


#ruta prueba
#C:\Users\Ismael\ISMAEL_CICLO_SUPERIOR\SEGUNDO DAM\PSP\teoria Phyton\SHELL.subprocces.pdf
# Usar subprocess para abrir el archivo con su programa predeterminado
subprocess.run(['cmd', '/c', 'start', '', file_path])
"""
cmd: Ejecuta el símbolo del sistema.
/c: Indica que se debe ejecutar el comando que sigue y luego terminar.
start: Es un comando que abre un archivo o ejecuta un programa.
'': Un argumento vacío que se requiere, pero no se usa para nada.
file_path: La ruta al archivo que deseas abrir.
Este método funcionará para cualquier tipo de archivo, siempre que haya un programa predeterminado asociado para abrirlo
"""
