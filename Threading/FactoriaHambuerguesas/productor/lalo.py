import random
import threading
import time
from threading import Thread, Semaphore

# este semaforo deja cocinar 5 burgers, representa las burgers q caben en el mostrador
s_cocineros = Semaphore(5)
#este semaforo hace que los camareros no empiecen al instante, representa las burgers q hay en el mostrador
s_camareros = Semaphore(0)

platos = 0

# cola FIFO
mostrador = []

def cocinero(id_cocinero, plato, mostrador):
    print(f"Cocinero {str(id_cocinero)} empieza a cocinar...")
    time.sleep(random.random()*3)

    print(f"Cocinero {str(id_cocinero)} suelta una burger...")

    # disminuimos en uno el value del semaforo de los cocineros, pues cabe en el mostrador una burger menos
    s_cocineros.acquire()

    # añadimos un plato al mostrador y se lo indicamos a los camareros con el release
    mostrador.append(plato)

    # aumentamos en 1 el value del semaforo de los camareros, pues hay una burger mas en el mostrador
    s_camareros.release()

    global platos
    platos += 1
    print("Platos en el mostrador: ", mostrador)



def camarero(id_camarero, mostrador):
    time.sleep(random.random()*3)
    print(f"Camarero {str(id_camarero)} espera por un plato...")

    # disminuimos en 1 el semaforo de los camareros, pues hay una burger menos en el mostrador
    s_camareros.acquire()
    # quitamos un plato en el mostrador
    mostrador.pop(0)
    # aumentamos en 1 el semaforo de los cocineros pues cabe en el mostrador una burger mas
    s_cocineros.release()

    print(f"Camarero {str(id_camarero)} lleva un plato...")

    global platos
    platos -= 1
    print("Platos en el mostrador: ", mostrador)



for i in range(10):
    plato = "Plato"+str(i)
    threading.Thread(target=cocinero, args=(i, plato, mostrador)).start()
    threading.Thread(target=camarero, args=(i, mostrador)).start()