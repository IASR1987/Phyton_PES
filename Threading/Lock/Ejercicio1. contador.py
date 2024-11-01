""": Ccounter=Noneama que use dos hilos para incrementar una variable compartida counter 10 veces
 cada uno. Usa Lock para proteger la variable compartida y evitar condiciones de carrera."""

import threading
import time

counter =0
#creamos el lock
lock = threading.Lock()

def aumentarCounter():

    #definimos la variable como global
    global counter


    """
    lock.acquire()
    
    for i in range(10):
        counter += 1
        print(counter)
        time.sleep(1)

    lock.release()
    """
    """CON  WITH LOCK"""
    """ejecutamos el primer hilo y después el segundo
    pq el lock se daquiere y se suelta cuando termina el bucle"""
    with lock:
        for i in range(10):
            print(threading.current_thread().name)
            counter += 1
            print(counter)
            time.sleep(1)
    """se adquiere el lock cada vez que entramos en el bucle y despues de una interaccion
    se libera, permite que los dos hilos se puedan ejecutar una vez uno y otra otro, superponiendose"""
    for i in range(10):
        with lock:
            print(threading.current_thread().name)
            counter += 1
            print(counter)
            time.sleep(1)

"""CREAMOS HILOS"""
hilo1=threading.Thread(target=aumentarCounter, name='hilo1 ', args=())
hilo2=threading.Thread(target=aumentarCounter, name='hilo 2', args=())

"""INICIAMOS LOS HILOS"""
hilo1.start()
hilo2.start()

"""ESPERAMOS QUE TERMINEN LOS HILOS PARA LA EJECUCION DEL PROGRAMA"""
hilo1.join()
hilo2.join()

print("Eso es todo amigos")

