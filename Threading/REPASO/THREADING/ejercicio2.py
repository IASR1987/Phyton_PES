"""Ejercicio 2: Crear un contador compartido
Implementa un contador que varios hilos incrementan 100 veces.
Cada hilo debe aumentar el contador global. Al final, imprime
el valor final del contador. Observa qué ocurre sin sincronización
y luego intenta con Lock en los siguientes ejercicios."""
import threading

contador = 0

def aumentarContador():
    global contador
    contador += 100
    print(contador)

hilos=[]

for i in range(100):
    hilo= threading.Thread(target=aumentarContador)
    hilos.append(hilo)
    hilo.start()

