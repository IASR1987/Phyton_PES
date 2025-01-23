
import threading
import time
from collections import deque

semaforoC= threading.Semaphore(5)
semaforoM=threading.Semaphore(0)
mostrador = deque()

def cocinero(id):
    semaforoC.acquire()
    print("Cocinero "+ str(id)+" Cocinando hamburguesa "+ str(id) )
    time.sleep(2)
    print("Hamburguesa puesta en la barra")
    mostrador.append("hamburguesa "+str(id))
    print("-------------------------------------")
    print("BARRA")
    print(mostrador)
    print("-------------------------------------")
    time.sleep(4)
    semaforoM.release()



def mesero(id):
    print("Mesero "+str(id)+" esperando en el salon")
    semaforoM.acquire()
    print("Mesero"+str(id)+" recoge la "+ mostrador[0])
    mostrador.popleft()
    print("-------------------------------------")
    print("BARRA")
    print(mostrador)
    print("-------------------------------------")
    time.sleep(4)
    semaforoC.release()



Cocineros= []
Meseros= []
for i in range(0,10):
    Cocineros.append(threading.Thread(target=cocinero,args=(i,)))
    Meseros.append(threading.Thread(target=mesero,args=(i,)))

for i in range(0, 10):
    Cocineros[i].start()
    Meseros[i].start()

for i in range(0,10):
    Cocineros[i].join()
    Meseros[i].join()

