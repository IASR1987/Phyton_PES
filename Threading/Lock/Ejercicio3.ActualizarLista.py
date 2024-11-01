"""
Crea una lista vacía y haz que dos hilos agreguen números
a la lista 10 veces cada uno. Usa Lock para proteger el acceso a la lista.
"""
import math
import threading
from random import random

#creamos la lista
lista = []
#creamos el candado
candado = threading.Lock()

def agregarNumero(lista):
    for i in range(10):
        with candado:
            lista.append( round(random()*10, 0))


hilo1 = threading.Thread(target=agregarNumero, args=[lista])

hilo2 = threading.Thread(target=agregarNumero, args=[lista])


hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
# Imprimimos la lista final
print("Lista final:", lista)