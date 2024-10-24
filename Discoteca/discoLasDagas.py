"""
En una discoteca popular, hay un portero encargado de controlar el acceso. La discoteca tiene un aforo
limitado de 5 personas. El portero permite que las personas entren a la discoteca solo si hay espacio
disponible, y si no, las personas deben esperar afuera hasta que alguien salga.

Cada persona que llega a la discoteca tiene que pedir permiso al portero para entrar. El portero
verifica si hay espacio disponible. Si hay espacio, deja pasar a la persona, y si no, la persona
debe esperar hasta que alguien salga. Después de disfrutar de la discoteca durante un tiempo,
las personas salen y el portero permite la entrada a las que estaban esperando.

Objetivos:
    Usar un semaforo para controlar el acceso a la discoteca, limitando el aforo a 5 personas.
    Simular el tiempo que cada persona pasa dentro de la discoteca de forma aleatoria.
    Cuando una persona sale de la discoteca, otra que estaba esperando puede entrar.
    Mostrar el estado del acceso, incluyendo cuándo una persona entra, está disfrutando
    dentro y cuándo sale de la discoteca.
"""
import random
import threading
import time


class Discoteca:
    def __init__(self):
        self.semaforo = threading.Semaphore(value=4)



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def entrarDiscoteca(self, discoteca):
        # Intentar entrar a la discoteca
        print(f"{self.nombre} está intentando entrar a la discoteca.")
        discoteca.semaforo.acquire()  # Espera a que haya lugar disponible
        print(f"{self.nombre} ha entrado a la discoteca.")
        time.sleep(random.randint(5, 10))  # Simula que la persona está en la discoteca por un tiempo
        print(f"{self.nombre} ha salido de la discoteca.")
        discoteca.semaforo.release()  # Libera el lugar


discoteca = Discoteca()

# Crear 10 personas
nombres = ["Maria", "Juan", "Ana", "Luis", "Pedro", "Sofía", "Carlos", "Lucía", "Diego", "Isabel"]
personas = [Persona(nombre) for nombre in nombres]

# Crear y empezar hilos para cada persona
hilos = []

for persona in personas:
    hilo = threading.Thread(target=persona.entrarDiscoteca, args=(discoteca,))
    hilos.append(hilo)
    hilo.start()  # Inicia el hilo inmediatamente