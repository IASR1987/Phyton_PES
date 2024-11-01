import random
import threading
import time

def entrar(id, portero):
    with portero:
        print("la persona" +str(id)+" está esperando ")
        time.sleep(random.randint(5, 10))
        print("la persona"+str(id)+ " sale de la discoteca")

semaforo = threading.Semaphore(5)
for i in range(15):
    hilo = threading.Thread(target=entrar, args=(i, semaforo,))
    hilo.start()


