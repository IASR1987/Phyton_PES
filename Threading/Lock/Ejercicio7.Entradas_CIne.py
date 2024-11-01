"""
Simula la compra de boletos de cine por varios hilos.
Usa Lock para proteger la variable que representa los boletos disponibles.
"""

import threading
import time

entradasDisponibles=10
candado=threading.Lock()

def comprarEntradas():
    global entradasDisponibles
    with candado:
        if(entradasDisponibles>0):
            print("entrada vendida")
            entradasDisponibles=entradasDisponibles-1
            time.sleep(2)
        else:
            print("entrada no disponible")

hilo=[]

for i in range(12):
    hilo.append(threading.Thread(target=comprarEntradas, name='hilo'+str(i)))

for hilo in hilo:
    hilo.start()
    hilo.join()

