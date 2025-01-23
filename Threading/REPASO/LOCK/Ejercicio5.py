"""
Ejercicio 5: Hacer un contador seguro
Repite el ejercicio del contador compartido, pero
esta vez usa un Lock para asegurar que los incrementos
no se pierdan. Ejecuta el código y comprueba que el
resultado final sea correcto.
"""
import threading

contador=0

candado=threading.Lock()

def aumentarContador():
    global contador
    with candado:
        contador += 100
        print(contador)

hilos =[]

for i in range(10):
    hilo=threading.Thread(target=aumentarContador)
    hilos.append(hilo)
    hilo.start()

for i in range(10):
    hilos[i].join()


print(f"contador Total {contador}")

