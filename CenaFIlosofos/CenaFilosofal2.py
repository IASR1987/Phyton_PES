import threading
import time
import random

# Clase Tenedor
class Tenedor:
    def __init__(self, id):
        """Inicializa un tenedor con un identificador y un lock para controlar el acceso."""
        self.id = id  # Asigna un identificador al tenedor
        self.ocupado = threading.Lock()  # Crea un lock controlar el acceso

    def cogerTenedor(self, timeout=2):
        """Intentamos coger el tenedor, retorna True/False."""
        return self.ocupado.acquire(timeout=timeout)  # Intenta adquirir el lock con un tiempo de espera, en nuestro caso hemos puesto dos segundos

    def soltarTenedor(self):
        """Libera el tenedor."""
        self.ocupado.release()  # Libera el lock para permitir que otros filósofos lo usen


# Creamos los tenedores
tenedores = [Tenedor(i) for i in range(5)]  # Crea una lista de 5 tenedores con identificadores del 0 al 4


# Clase Filosofo
class Filosofo(threading.Thread):
    def __init__(self, id, nombre):
        """Inicializa un filósofo con un id y un nombre."""
        threading.Thread.__init__(self)  # Llama al constructor de la clase Thread
        self.id = id  # Asigna un identificador al filósofo
        self.nombre = nombre  # Asigna un nombre al filósofo
        # Asigna los tenedores izquierdo y derecho basándose en el id del filósofo
        self.tenedorDerecho = tenedores[(id - 1)]
        self.tenedorIzquierdo = tenedores[id % 5]

    def pensando(self):
        print(f"{self.nombre} pensando...")  # Imprime que el filósofo está pensando
        time.sleep(random.randint(10, 15))  # tiempo aleatorio entre 10 y 15 segundos

    def cogerTenedorF(self):
        """Intenta coger los tenedores en un orden específico para evitar deadlock."""
        """esto se denomina asignación múltiple que es una característica de Python que nos permite 
        asignar valores a múltiples variables en una sola línea."""
        if self.id % 2 == 0:  # Si el id es par
            primero, segundo = self.tenedorIzquierdo, self.tenedorDerecho  # Primero coge el izquierdo
        else:  # Si el id es impar
            primero, segundo = self.tenedorDerecho, self.tenedorIzquierdo  # Primero coge el derecho

        # Intenta coger el primer tenedor
        if primero.cogerTenedor():  # Intenta adquirir el primer tenedor, si es par el izquierdo si es impar el derecho
            print(f"{self.nombre} ha cogido el tenedor {primero.id}")  # Imprime que ha cogido el tenedor
            time.sleep(2)  # Espera un poco antes de intentar coger el segundo
            if segundo.cogerTenedor():  # Intenta coger el segundo tenedor
                print(f"{self.nombre} ha cogido el tenedor {segundo.id}")  # Imprime que ha cogido el segundo tenedor
                return True  # Retorna True si ha podido coger ambos tenedores
            else:
                """sino puede coger el segundo antes del timeout, soltará el primero"""
                primero.soltarTenedor()  # Suelta el primer tenedor si no puede coger el segundo
                print(f"{self.nombre} ha soltado el tenedor {primero.id} porque no pudo coger el segundo.")
        return False  # Retorna False si no pudo coger ambos tenedores

    def soltarTenedorF(self):
        """Suelta ambos tenedores."""
        self.tenedorDerecho.soltarTenedor()  # Suelta el tenedor derecho
        self.tenedorIzquierdo.soltarTenedor()  # Suelta el tenedor izquierdo
        print(f"{self.nombre} deja de comer.")  # Imprime que deja de comer
        time.sleep(1)
        print(f"{self.nombre} ha soltado ambos tenedores.")  # Imprime que ha soltado los tenedores

    def run(self):
        """Métdo que se ejecuta cuando se inicia el hilo del filósofo"""
        while True:  # Ciclo infinito para simular la vida del filósofo
            self.pensando()  # Filósofo comienza a pensar
            if self.cogerTenedorF():  # Intenta coger los tenedores
                print(f"{self.nombre} está comiendo.")  # Imprime que el filósofo está comiendo
                time.sleep(5)  # Simula el tiempo que pasa comiendo
                self.soltarTenedorF()  # Libera los tenedores después de comer
            else:
                print(f"{self.nombre} seguirá pensando.")  # Imprime que seguirá pensando si no puede comer


# Lista de nombres de los filósofos
nombres = ["Sócrates", "Platón", "Aristóteles", "Heráclito", "Epicuro"]

# Crear los filósofos
filosofos = [Filosofo(i + 1, nombres[i]) for i in range(5)]  # Crea una lista de filósofos

# Iniciar los hilos de filósofos
for filosofo in filosofos:
    filosofo.start()

