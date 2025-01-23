"""Ejercicio 14: Sincronización de tareas en una fábrica
Simula una cadena de montaje en una fábrica donde los
trabajadores (hilos) deben terminar sus tareas en sincronía.
Cada trabajador debe esperar en una barrera hasta que todos
hayan completado una tarea antes de pasar a la siguiente.
"""
import random
import threading
import time

numeroEmpleado=random.randint(3,5)

tarea1= threading.Barrier(numeroEmpleado)
tarea2= threading.Barrier(numeroEmpleado)
tarea3= threading.Barrier(numeroEmpleado)

def Tarea1(id):
    print(f"empleado {id} esta realizando la tarea1")
    time.sleep(random.randint(3,6))
    tarea1.wait()
    print(f"empleado {id} ha terminado la tarea1")
    time.sleep(1)

def Tarea2(id):
    print(f"empleado {id} esta realizando la tarea2")
    time.sleep(random.randint(3,6))
    tarea2.wait()
    print(f"empleado {id} ha terminado la tarea2")

def Tarea3(id):
    print(f"empleado {id} esta realizando la tarea3")
    time.sleep(random.randint(3,6))
    tarea3.wait()
    print(f"empleado {id} ha terminado la tarea3")

def fabricarProducto(id):
    Tarea1(id)
    Tarea2(id)
    Tarea3(id)
    print(f"empleado {id} ha hecho un coche{id}.")

empleados=[]

for i in range(numeroEmpleado):
    empleado = threading.Thread(target=fabricarProducto, args=(i,))
    empleado.start()
    empleados.append(empleado)

for empleado in empleados:
    empleado.join()