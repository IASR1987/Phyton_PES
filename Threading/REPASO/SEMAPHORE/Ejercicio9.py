"""
Ejercicio 9: Simulación de impresoras
Imagina que tienes 2 impresoras en una oficina y 5 empleados
que desean imprimir documentos. Usa Semaphore para controlar
que solo dos hilos (empleados) puedan "usar" las impresoras al mismo tiempo.
"""
import threading
import time

semaforo = threading.Semaphore(2)

def impresoras(id):
    print(f"empleado ${id} quiere imprimir")
    time.sleep(1)
    #adquirimos el semáforo
    semaforo.acquire()
    print(f"empleado ${id} esta imprimiendo")
    time.sleep(2)
    print(f"empleado ${id} ha terminado")
    semaforo.release()


empleados = []

for i in range(5):
    empleado= threading.Thread(target=impresoras, args=(i,))
    empleado.start()
    empleados.append(empleado)

for empleado in empleados:
    empleado.join()

print("Todo terminado")
