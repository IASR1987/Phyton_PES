import subprocess
import time

# Usar 'start' para abrir Notepad
print("Abriendo Notepad con start...")
subprocess.run(['start', 'notepad.exe'], shell=True)

# Código seguirá ejecutándose inmediatamente
print("El script continúa ejecutándose...")

# Pausa para mostrar el comportamiento
time.sleep(5)

# Usar Notepad directamente
print("Abriendo Notepad directamente...")
subprocess.run(['notepad.exe'])

# Este mensaje no se mostrará hasta que Notepad se cierre
print("Este mensaje aparece después de cerrar Notepad.")
"""
Uso de start: No bloquea el script y permite que continúe mientras Notepad está abierto.
Uso directo de Notepad.exe: Bloquea el script hasta que se cierre Notepad."""
"""
TEORÍA
Diferencias Clave:

    Comportamiento del proceso:
        start:
            Utiliza el comando start, que es un comando interno de la consola de Windows. 
            Este comando abrirá Notepad en una nueva ventana y no bloqueará el script de Python;
            es decir, el control regresará al script inmediatamente, permitiéndole continuar con 
            la ejecución de cualquier otra línea de código.
        Sin start:
            Al ejecutar directamente Notepad.exe, el script de Python esperará a que Notepad se 
            cierre antes de continuar con la siguiente línea de código. Esto significa que el script 
            se detendrá hasta que el usuario cierre Notepad.

    Tipo de ventana:
        start:
            Al usar start, Notepad se abrirá en una nueva ventana, que es independiente del proceso 
            que ejecuta el script de Python.
        Sin start:
            Notepad se abrirá en la misma ventana de consola de Python, aunque visualmente se vea 
            como una aplicación independiente.

    Uso de shell:
        En ambos casos, se utiliza shell=True, lo que permite que el comando start funcione correctamente.
        Sin embargo, si se omite el uso de shell=True en el primer comando, recibirás un error porque start
        no es reconocido como un comando por subprocess sin el shell.
"""