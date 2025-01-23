import random
import threading
import time


semaforoC= threading.Semaphore(5)
semaforoM=threading.Semaphore(0)

def cocinero(id, platos=5):
    semaforoC.acquire()
    print("Cocinero "+ str(id)+" Cocinando hamburguesa")
    print("Hamburguesa puesta en la barra")
    print("-------------------------------------")
    semaforoM.release()
    platos += 1
    print("platos hechos "+ str(platos))


def mesero(id, platos=5):
    print("Mesero "+str(id)+" esperando en el salon")
    time.sleep(random.randint(2,4))
    semaforoM.acquire()
    print("Mesero"+str(id)+" recoge la hamburguesa")
    platos -= 1
    print("platos retirados " + str(platos))
    time.sleep(random.randint(5,5))
    semaforoC.release()



Cocineros= []
Meseros= []
for i in range(0,10):
    Cocineros.append(threading.Thread(target=cocinero,args=(i,)))
    Meseros.append(threading.Thread(target=mesero,args=(i,)))

for i in range(0, 10):
    Meseros[i].start()
    Cocineros[i].start()

for i in range(0,10):
    Cocineros[i].join()
    Meseros[i].join()

