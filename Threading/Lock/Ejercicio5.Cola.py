"""
Imagina que estás gestionando una fábrica donde los productos son creados (producidos)
por un trabajador (productor) y luego son empaquetados (consumidos) por otro trabajador (consumidor).
Debes implementar dos hilos en Python:

FactoriaHambuerguesas: Este hilo generará (producirá) un número fijo de productos y los agregará a una cola compartida.
Consumidor: Este hilo tomará productos de la cola compartida y los "consumirá".

"""
import threading
import time

from collections import deque

#lista que agrega y borra en el principio o el final
productos = deque()
candado= threading.Lock()


def producirProducto(productos):
    for i in range(11):
        with candado :
            productos.append(1)
            print("producto producido")
            time.sleep(2)
            print("longitud de la cola es " + str(len(productos)))


def consumirProducto(productos):
    for i in range(11):
        with candado :
            productos.popleft()
            print("producto consumido")
            time.sleep(4)
            print("longitud de la cola es "+ str(len(productos)))


hilo1=threading.Thread(target=producirProducto, args=(productos,))
hilo2= threading.Thread(target=consumirProducto, args=(productos,))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

