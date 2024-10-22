import threading
from threading import *
import time



class Cocinero(threading.Thread):
    def __init__(self, nombre, plato, tiempo_preparacion):
        super().__init__()  # Llamada al constructor de la clase padre threading.Thread
        self.nombre = nombre  # Almacena el nombre del cocinero
        self.plato = plato  # Almacena el plato que el cocinero va a preparar
        self.tiempo_preparacion = tiempo_preparacion  # Almacena el tiempo de preparación del plato


