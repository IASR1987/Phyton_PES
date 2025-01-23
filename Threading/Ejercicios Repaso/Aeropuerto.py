import random
import threading
import time


pista = threading.Semaphore(2)
barrera = threading.Barrier(2)
climatologia = threading.Event()

def clima():
    while True:
        numero = random.randint(1, 10)
        print(numero)
        if numero > 5:
            climatologia.set()
            print("tiempo malo")
            time.sleep(5)
            print("Evaluamos el tiempo")
        else:
            climatologia.set()
            print("tiempo bueno")
            time.sleep(5)
            climatologia.clear()
            print("Evaluamos el tiempo")
        time.sleep(numero)


def despegar(id):
    pista.acquire()
    print("Avión "+ str(id )+" Entrando en pista")
    time.sleep(2)
    barrera.wait()
    print("Avion " + str(id) + " En mantenimiento")
    time.sleep(2)
    print("Avion " + str(id) + " listo")

    if climatologia.is_set():
        print("Tiempo malo para el avion "+str(id))
        time.sleep(random.randint(9,10))
        climatologia.clear()
        if not climatologia.is_set():
            print("Avión " + str(id) + " despegando")
            pista.release()
    else:
        print("tiempo bueno para el despegue del  avion "+str(id))
        print("Avión " + str(id) + " despegando")
        time.sleep(random.randint(2, 4))
        pista.release()


Aviones=[]

hilo_clima = threading.Thread(target=clima, daemon=True)
hilo_clima.start()

for i in range(11):
    Aviones.append(threading.Thread(target=despegar, args=(i,)))
    Aviones[i].start()
