"""
Ejercicio 8: Productor-consumidor simple
Implementa el problema de productor-consumidor.
Crea un productor que genere números aleatorios y los
coloque en una lista compartida, y un consumidor que
retire números de la lista.
Usa Semaphore para sincronizar el acceso entre productor y consumidor.
"""
import random
import threading
import time

#semaforo controla el acceso a lista
acceso = threading.Semaphore(1)
#semaforo que indica si hay producto en la lista aumentando el semaphore con el release
producto = threading.Semaphore(0)

#lista de numeros
lista=[]



def productor(lista,numero):
    acceso.acquire()
    print(f"añadimos el {numero} a la lista")
    lista.append(numero)
    acceso.release()
    producto.release()

def consumidor(lista):
    producto.acquire()
    acceso.acquire()
    if lista:
        print(f"borramos el {lista[0]} de la lista.")
        lista.pop(0)
    acceso.release()

hilos=[]

for i in range(10):
    p=threading.Thread(target=productor,args=(lista,random.randint(1,100),))
    c=threading.Thread(target=consumidor,args=(lista,))
    p.start()
    c.start()
    hilos.append(p)
    hilos.append(c)

for hilos in hilos:
    hilos.join()

print(lista)