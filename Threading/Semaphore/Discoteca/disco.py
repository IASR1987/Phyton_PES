import random
import threading
import time

portero= threading.Semaphore(5)

def entrar(id, portero):
    print("la persona" + str(id) + " está EN LA COLA ")
    time.sleep(1)
    with portero:
        print("la persona "+str(id)+" ENTRA en la discoteca")
        time.sleep(random.randint(5, 10))
        print("la persona "+str(id)+ " sale de la discoteca")


hilos = []
for i in range(15):
    hilo = threading.Thread(target=entrar, args=(i, portero,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()



