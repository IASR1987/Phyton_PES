"""
Ejercicio 6: Hacer un contador con decrementos y un límite
Crea dos tipos de hilos: unos que incrementan un contador y
otros que lo decrementan. Usa un Lock para asegurar que no
haya condiciones de carrera. Alcanza un límite máximo (por
ejemplo, 10) en el contador para que los hilos de incremento se detengan una vez alcanzado.
"""
import random
import threading

contador = 10

numero=10

candado = threading.Lock()

def incremento():
    global contador
    global numero

    candado.acquire()
    numero=numero+(random.randint(1,10))
    candado.release()
    print(f"{numero} tras incremento")

def decremento():
    global contador
    global numero

    candado.acquire()
    contador -= 1
    numero=numero-(random.randint(1,10))
    candado.release()
    print(f"{numero} tras decremento")


hilosIncremento=[]
hilosDecremento=[]


for i in range(20):
    if(contador >0):
        hilo = threading.Thread(target=incremento)
        hilo1 = threading.Thread(target=decremento)
        hilosIncremento.append(hilo)
        hilosDecremento.append(hilo1)
        hilo.start()
        hilo1.start()
    else:
        hilo = threading.Thread(target=incremento)
        hilosIncremento.append(hilo)
        hilo.start()