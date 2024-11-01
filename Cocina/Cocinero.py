"""Un restaurante muy popular cuenta con varios cocineros que trabajan en paralelo
para preparar distintos platos. Cada cocinero es responsable de preparar un plato específico,
y estos cocineros pueden trabajar al mismo tiempo. Sin embargo, no se puede servir la comida
hasta que todos los cocineros hayan terminado de preparar sus platos.
Tu tarea es simular este escenario usando  en Python para representar a los cocineros. Cada
cocinero tardará un tiempo diferente en preparar su plato, y cuando todos hayan terminado,
se podrá servir la comida.Objetivos:

Crear una clase Cocinero que extienda de threading.Thread para representar a cada cocinero como un hilo.
Asignar a cada cocinero un plato para preparar y simular el tiempo de preparación utilizando time.sleep().
Todos los cocineros deben trabajar en paralelo y preparar sus platos.
Utilizar el mét-odo join() para asegurarse de que todos los cocineros terminen de preparar sus platos
antes de poder servir la comida.
Una vez que todos los cocineros hayan terminado, imprimir un mensaje indicando que todos los platos están
listos para ser servidos.

Requisitos:

Implementa una lista con al menos 4 platos diferentes que los cocineros deben preparar (pueden ser: "Pizza",
"Pasta", "Hamburguesa", "Ensalada").
Cada cocinero tendrá un tiempo de preparación aleatorio para su plato (por ejemplo, entre 3 y 7 segundos).
La salida del programa debe mostrar cuándo cada cocinero empieza a preparar su plato, cuándo termina, y
finalmente un mensaje que indique que todos los platos están listos para ser servidos."""

import threading
import time
import random

class Cocinero(threading.Thread):
    def __init__(self, nombre, plato):
        super().__init__()  # Llamada al constructor de la clase padre threading.Thread
        self.nombre = nombre  # Almacena el nombre del cocinero
        self.plato = plato  # Almacena el plato que el cocinero va a preparar
        self.tiempoPreparacion = random.randint(1, 4)  # Almacena el tiempo de preparación del plato

    def run(self):
        time.sleep(self.tiempoPreparacion)
        print(self.tiempoPreparacion)
        print(self.nombre)
        print(self.plato)

Cocineros =[]
platos = ["Pizza", "Pasta", "Hamburguesa", "Ensalada"]
nombre = ["Luigi","Mario","Arguiñano","Arzak"]

# Crear instancias de Cocinero y agregarlas a la lista
for i in range(4):
    Cocineros.append(Cocinero(nombre[i], platos[i]))

# Iniciar todos los hilos
for cocinero in Cocineros:
    cocinero.start()

# Esperar a que todos los hilos terminen
for cocinero in Cocineros:
    cocinero.join()

print('Todos los platos están listos, pueden comenzar a servir')