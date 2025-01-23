"""Ejercicio 1: Crear varios hilos simples
Crea un programa que lance 5 hilos, cada uno imprimiendo su número
y el mensaje "Hilo iniciado". Cada hilo debe esperar un tiempo aleatorio
entre 1 y 3 segundos antes de terminar. Al final, imprime "Todos los
hilos han terminado".
"""
import random
import threading
import time


def hiloInicial(id):
    print(f"Hilo ${id} iniciado")
    time.sleep(random.randint(1, 3))
    print(f"Hilo ${id} terminado")

hilos=[]

#creamos 5 hilos
for i in range(5):
    hilo= threading.Thread(target=hiloInicial, args=(i,));
    hilos.append(hilo)
    hilo.start()

