"""
Simulación de una luz de tráfico
Simula una luz de tráfico con Event.
Crea un hilo de luz de tráfico que cambie
de rojo a verde cada 5 segundos. Crea
varios hilos de autos que deben detenerse
si la luz está en rojo y avanzar cuando está en verde.
"""
import random
import threading
import time

semaforo = threading.Event()
contador=10

def sema():
    while contador>0:
        print("EL SEMAFORO ESTÁ EN ROJO")
        time.sleep(3)
        semaforo.set()
        print("EL SEMAFORO SE PONE EN VERDE")
        time.sleep(5)
        semaforo.clear()

def cruzando(id):
    global contador
    print(f"coche{id} llega al semáforo")
    semaforo.wait()
    contador-=1
    print(f"coche{id} pasando")

coches=[]
semaf= threading.Thread(target=sema)
semaf.start()

for i in range(contador):
    time.sleep(1)
    coche=threading.Thread(target=cruzando, args=(i,))
    coches.append(coche)
    coche.start()



for coche in coches:
    coche.join()


print("todos los coches han pasado")
print(contador)

