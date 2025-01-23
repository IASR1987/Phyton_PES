"""
Ejercicio 4: Control de acceso a una lista compartida
Crea un programa donde 5 hilos intentan agregar elementos
a una lista compartida. Usa Lock para sincronizar el acceso
a la lista, de modo que solo un hilo pueda agregar un elemento a la vez
"""
import threading
import random

#lista para agregar elementos
lista=[]
#creamos el candado que hace que la lista solo pueda ser una
candado= threading.Lock()

def agregarElementos(lista, numero):
    with candado:
        lista.append(numero)
        print(f"{numero} agregado a la lista.")


hilos =[]
for i in range(5):
    numero=random.randint(1,100)
    hilo= threading.Thread(target=agregarElementos, args=(lista,numero))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()
    
print(lista)