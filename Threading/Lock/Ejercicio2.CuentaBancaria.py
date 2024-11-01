"""
Enunciado: Simula una cuenta bancaria donde dos hilos intentan realizar
depósitos y retiros de una variable balance. Usa Lock para proteger el saldo.
"""

import threading
import time
from threading import Thread


saldo=1000
print("saldo Inicial "+ str(saldo))
candado= threading.Lock()

def sacarDinero(retiro):
    global saldo
    with candado:
        saldo -= retiro

def ingresarDinero(ingreso):
    global saldo
    with candado:
        saldo += ingreso


hilo1= threading.Thread(target=sacarDinero, args=(30,))
hilo2= threading.Thread(target=ingresarDinero, args=(60, ))

hilo1.start()
print("saldo tras retirar dinero "+ str(saldo))
hilo2.start()

print("saldo Final "+ str(saldo))