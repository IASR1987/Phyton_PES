
import subprocess

# El título de la ventana se coloca como una cadena vacía ("") antes de la URL.
#subprocess.run(['start', '', 'https://www.google.com'], shell=True)

subprocess.run(['start', 'Notepad.exe'], shell=True)

subprocess.run(['Notepad.exe'], shell=True)
