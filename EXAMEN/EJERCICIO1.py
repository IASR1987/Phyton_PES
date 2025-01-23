import random
import threading
import time

#grupo exploradores
grupo_exploradores=5

#numeroExploradores total
grupo=15

#barrera que bloquea el paso de los exploradores
pasoDesierto = threading.Barrier(grupo_exploradores)

#EVENTO QUE REGULA LOS ASESINOS
acecho= threading.Event()


def pasoDelDesierto(id):
    print(f"explorador {id} comienza su trayecto")
    #tiempo en llegar al paso
    time.sleep(random.randint(6,10))
    print(f"explorador {id} llega a la barrera")

    try:
        #esperamos que lleguen los compañeros
        pasoDesierto.wait()
        print(f"explorador {id} junto a su grupo PASA DESIERTO")
        time.sleep(1)
    except threading.BrokenBarrierError:#rompe la barrera mueren todos los explradores
        print(f"explorador {id} MUERE DEGOLLADO a mano de los salvajes.")

def muerteExplorador():
    while True:
        time.sleep(6)
        print("los salvajes vigilan la caravana")
        time.sleep(4)
        print("SANGRE Y FUEGO")
        #rompe la barrera, slata el error en pasoDelDesierto
        pasoDesierto.reset()


# hilo que representa a los salvajes
Asesinos= threading.Thread(target=muerteExplorador, daemon=True)#daemon para que termine
#inicia el hilo
Asesinos.start()

#lista para exploradores
Caravana = []

#creamos hilos y los iniciamos, lo agregamos a la lista
for i in range(grupo):
    explorador= threading.Thread(target=pasoDelDesierto, args=(i,))
    explorador.start()
    Caravana.append(explorador)

#esperamos que terminen los hilos
for explorador in Caravana:
    explorador.join()

print("FIN DE LA PELÍCULA")