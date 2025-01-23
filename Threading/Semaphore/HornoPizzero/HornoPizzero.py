"""Igual que el ejercicio de los cocineros pero con un horno que admite
2 pizzas y 6 cocineros con sus pizzas"""
import random
import threading
import time
"""
Vamos a explicar cada uno:

threading.BoundedSemaphore(value=pizzasHorno):
    BoundedSemaphore es una versión especial de Semaphore que asegura que
    nunca se libere más veces de las que se adquirió, lo cual es útil para
    asegurarse de que la cantidad de recursos nunca exceda un valor máximo predefinido.
    Usar BoundedSemaphore sería útil en casos donde quieras asegurarte de que
    el recurso no se libere de manera accidental más veces de las que fue adquirido.

threading.Semaphore(pizzasHorno):
    Semaphore es un semáforo regular, que permite hasta un número definido de 
    "permisos" para acceder a un recurso compartido.
    No impone ninguna restricción adicional sobre la cantidad de veces que el 
    recurso puede ser liberado.
"""

pizzasHorno =2
semaforo= threading.BoundedSemaphore(value=pizzasHorno)
#semaforo=threading.Semaphore(pizzasHorno)


class Cocinero(threading.Thread):
    def __init__(self, nombre, tipoPizza):
        super().__init__()  # Llamar al constructor de la clase base threading.Thread
        self.nombre = nombre
        self.tipoPizza = tipoPizza
        self.tiempoPreparacion= random.randint(3,10)

    def run(self):
        with semaforo:
            print(f'El cocinero {self.nombre}  está metiendo su pizza {self.tipoPizza} en el horno')
            time.sleep(1)
            print('Pizza cocinandose')
            time.sleep(self.tiempoPreparacion)
            print(f'la pizza {self.tipoPizza} esta preparada')



pizzas = ('peperonni', 'margarita', 'cuatro quesos', 'barbacoa', 'carbonara', 'pesto')
nombresCocineros = ('Pepe','Luigi','Luca','Flavio', 'Gennaro','Andrea')
listaChefs=[]

for i in range(6):
    cocinero=Cocinero(nombresCocineros[i], pizzas[i])
    listaChefs.append(cocinero)
    cocinero.start()

for cocinero in listaChefs:
    cocinero.join()

print('Trabajo terminado')