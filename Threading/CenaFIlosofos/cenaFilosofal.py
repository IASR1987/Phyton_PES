"""
Cinco filósofos se sientan alrededor de una mesa y pasan su vida cenando y pensando.
Cada filósofo tiene un plato de fideos y un tenedor a la izquierda de su plato.
Para comer los fideos son necesarios dos tenedores y cada filósofo sólo puede tomar
los que están a su izquierda y derecha. Si cualquier filósofo toma un tenedor y el otro
está ocupado, se quedará esperando, con el tenedor en la mano, hasta que pueda tomar el
otro tenedor, para luego empezar a comer.

Si dos filósofos adyacentes intentan tomar el mismo tenedor a una vez, se produce una
condición de carrera: ambos compiten por tomar el mismo tenedor, y uno de ellos se queda sin comer.

Si todos los filósofos toman el tenedor que está a su derecha al mismo tiempo, entonces
todos se quedarán esperando eternamente, porque alguien debe liberar el tenedor que les falta.
Nadie lo hará porque todos se encuentran en la misma situación (esperando que alguno deje sus tenedores).
Entonces los filósofos se morirán de hambre. Este bloqueo mutuo se denomina interbloqueo o deadlock.
El problema consiste en encontrar un algoritmo que permita que los filósofos nunca se mueran de hambre.


Reglas:
    Cinco filósofos están sentados en una mesa redonda, alternando entre comer y pensar.
    Cinco tenedores están ubicados entre los platos, uno entre cada par de filósofos.
    Para comer, un filósofo debe tener ambos tenedores (el de su izquierda y el de su derecha).
    Solo un filósofo puede usar un tenedor a la vez.
    Cuando un filósofo ha terminado de comer, debe soltar ambos tenedores para permitir que los otros filósofos coman.
    Si todos los filósofos intentan comer al mismo tiempo y toman el tenedor a su izquierda, se produce un (bloqueo), ya que ninguno puede tomar su segundo tenedor.

Objetivo:
El objetivo es diseñar un algoritmo que permita que todos los filósofos coman sin que se
produzca un deadlock (bloqueo mutuo), y garantizando que ningún filósofo se quede sin comer
indefinidamente (starvation).Preguntas a resolver:

¿Cómo pueden sincronizarse los filósofos para evitar que todos intenten tomar los mismos
tenedores al mismo tiempo?¿Cómo evitar que un filósofo se quede esperando indefinidamente
si los tenedores no están disponibles (evitar el starvation)?Condiciones adicionales:
    Los filósofos deben alternar entre los estados de pensar y comer.
    No se puede tener más de un filósofo usando el mismo tenedor simultáneamente.
    Cada filósofo debe poder eventualmente comer, evitando situaciones donde alguno nunca pueda hacerlo.

Sugerencias:
    Usa semaforos o locks para controlar el acceso a los tenedores.
    Considera soluciones como que no todos los filósofos tomen los tenedores en el mismo orden
    (por ejemplo, algunos podrían intentar tomar primero el tenedor de la derecha y otros el de la izquierda).
    También podrías considerar limitar el número de filósofos que pueden intentar comer al mismo
    tiempo para reducir la posibilidad de deadlock
"""

import threading
import time
import random

# Clase Tenedor
class Tenedor:
    def __init__(self, id):
        """Inicializa un tenedor con un identificador y un lock para controlar el acceso."""
        self.id = id  # Asigna un identificador al tenedor
        self.ocupado = threading.Lock()  # Crea un lock

    def cogerTenedor(self):
        """Intenta coger el tenedor."""
        self.ocupado.acquire()  # Adquiere el lock para usar el tenedor

    def soltarTenedor(self):
        """Suelta el tenedor."""
        self.ocupado.release()  # Libera el lock para permitir que otros filósofos lo usen


# Crear los tenedores
tenedores = []  # Lista para almacenar los tenedores
for i in range(5):  # Crea 5 tenedores
    tenedores.append(Tenedor(i))

# Clase Filosofo
class Filosofo(threading.Thread):
    def __init__(self, id, nombre):
        """Inicializa un filósofo con un id y un nombre."""
        threading.Thread.__init__(self)
        self.id = id
        self.nombre = nombre
        # Asigna los tenedores izquierdo y derecho basándose en el id del filósofo
        self.tenedorDerecho = tenedores[(id - 1)]  # Tenedor a la derecha
        self.tenedorIzquierdo = tenedores[id % 5]  # Tenedor a la izquierda

    def pensando(self):
        """Filosofo pensando"""
        print(f"{self.nombre} pensando...")  # Imprime que el filósofo está pensando
        time.sleep(random.randint(10, 15))  # Espera un tiempo aleatorio entre 10 y 15 segundos

    def cogerTenedor(self):
        """Intenta coger los tenedores en un orden específico."""
        # Si el id del filósofo es par, intenta coger primero el tenedor de la derecha, luego el de la izquierda
        if self.id % 2 == 0:
            self.tenedorDerecho.cogerTenedor()  # Intenta adquirir el tenedor derecho
            print(f"{self.nombre} está cogiendo el tenedor {self.id - 1}")
            self.tenedorIzquierdo.cogerTenedor()  # Intenta adquirir el tenedor izquierdo
            print(f"{self.nombre} está cogiendo el tenedor {self.id % 5}")
        else:
            # Si el id del filósofo es impar, intenta coger primero el tenedor de la izquierda, luego el de la derecha
            self.tenedorIzquierdo.cogerTenedor()  # Intenta adquirir el tenedor izquierdo
            print(f"{self.nombre} está cogiendo el tenedor {self.id % 5}")
            self.tenedorDerecho.cogerTenedor()  # Intenta adquirir el tenedor derecho
            print(f"{self.nombre} está cogiendo el tenedor {self.id - 1}")

        print(f"{self.nombre} está comiendo")  # Imprime que el filósofo está comiendo
        time.sleep(10)  # Simula el tiempo que pasa comiendo

    def soltarTenedor(self):
        """Libera ambos tenedores."""
        self.tenedorDerecho.soltarTenedor()  # Libera el tenedor derecho
        print(f"{self.nombre} está soltando el tenedor {self.id - 1}")  # Imprime que está soltando el derecho
        time.sleep(4)  # Espera un momento antes de soltar el izquierdo

        self.tenedorIzquierdo.soltarTenedor()  # Libera el tenedor izquierdo
        print(f"{self.nombre} está soltando el tenedor {self.id % 5}")  # Imprime que está suelta el izquierdo

    def run(self):
        """Métdo que se ejecuta cuando se inicia el hilo del filósofo."""
        while True:  # Ciclo infinito para simular la vida del filósofo
            self.pensando()  # Filósofo comienza a pensar
            self.cogerTenedor()  # Se intenta coger los tenedores
            self.soltarTenedor()  # Se sueltan los tenedores después de comer


# Lista de nombres de los filósofos
nombres = ["Sócrates", "Platón", "Aristóteles", "Heráclito", "Epicuro"]

# Crear los filósofos
filosofos = [Filosofo(i + 1, nombres[i]) for i in range(5)]

# Iniciar los hilos de filósofos
for i in range(5):
    filosofos[i].start()

