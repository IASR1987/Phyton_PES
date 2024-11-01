"""
Ejercicio 6: Contador con Incrementos y Decrementos

Enunciado: Haz que dos hilos incrementen y otros dos hilos
decrementen una variable compartida counter 10 veces.
Usa Lock para sincronizar los hilos.
"""
import threading
import time

contador=0

candado=threading.Lock()

def incremento():
    global contador
    with candado:
        contador+=1
        print("incremento "+ str(contador))
        time.sleep(2)
        print(threading.current_thread().name)

def decremento():
    global contador
    with candado:
        contador-=1
        print("decremento "+ str(contador))
        time.sleep(2)
        print(threading.current_thread().name)

hilo1=threading.Thread(target=incremento, name='hilo1',)
hilo2=threading.Thread(target=decremento, name='hilo2',)
hilo3=threading.Thread(target=incremento, name='hilo3',)
hilo4=threading.Thread(target=decremento, name='hilo4',)

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

print('Eso es todo amigos')