import threading
import time


semaforoC= threading.Semaphore(5)
semaforoM=threading.Semaphore(0)
mostrador = []
candado = threading.Lock

def cocinero(id):
    semaforoC.acquire()
    print("Cocinero "+ str(id)+" Cocinando hamburguesa "+ str(id) )
    print("Hamburguesa puesta en la barra")
    mostrador.append("hamburguesa "+str(id))
    print("-------------------------------------")
    print("BARRA")
    print(mostrador)
    print("-------------------------------------")
    time.sleep(2)
    semaforoM.release()



def mesero(id):
    print("Mesero "+str(id)+" esperando en el salon")
    semaforoM.acquire()
    print("Mesero"+str(id)+" recoge la "+ mostrador[0])

    mostrador.pop(0)
    print("-------------------------------------")
    print("BARRA")
    print(mostrador)
    print("-------------------------------------")
    semaforoC.release()



Cocineros= []
Meseros= []
for i in range(0,20):
    Cocineros.append(threading.Thread(target=cocinero,args=(i,)))
    Meseros.append(threading.Thread(target=mesero,args=(i,)))

for i in range(0, 20):
    Cocineros[i].start()
    Meseros[i].start()

for i in range(0,20):
    Cocineros[i].join()
    Meseros[i].join()