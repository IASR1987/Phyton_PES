"""
Imagina que tienes un rebaño de ovejas que deben cruzar un valle en grupos
para llegar a una zona segura. Para minimizar el riesgo, todas las ovejas
deben esperar a que el grupo completo esté listo para cruzar, y así se mueven
juntas. Una vez que todas las ovejas de un grupo están preparadas, cruzan el valle
al mismo tiempo. A los 10 segundos de ejecución, llegará un lobo a la zona de
espera y se dará un festín.

Este proceso se repetirá hasta que todas las ovejas hayan cruzado. Para simular esto,
utilizaremos  en Python. Cada grupo de ovejas se sincronizará en la barrera antes de cruzar.
Si una oveja llega a la barrera y no todas están listas, debe esperar hasta que todas las
demás estén preparadas. Una vez que todas las ovejas están en la barrera, el grupo cruza
el valle y se prepara para la siguiente etapa.
"""
import threading
import time
import random

# Número total de ovejas y tamaño de los grupos
NUM_OVELAS = 100
TAMANO_GRUPO = 3

# Barrera que sincroniza a las ovejas en cada cruce
barrera = threading.Barrier(TAMANO_GRUPO)


def oveja(id_oveja):
    print(f"Oveja {id_oveja} llega a la zona de espera.")
    try:
        # Simula que la oveja llega a la barrera y espera al resto del grupo
        tiempo_espera = random.uniform(0.5, 2.0)  # Tiempo aleatorio para simular la llegada
        time.sleep(tiempo_espera)
        print(f"Oveja {id_oveja} está lista para cruzar y espera al grupo.")

        # La oveja espera hasta que todas en el grupo estén listas
        barrera.wait()

        print(f"Oveja {id_oveja} cruza el valle.")

    except threading.BrokenBarrierError:
        print(f"Oveja {id_oveja} fue capturada por el lobo.")


def lobo():
    # Espera 10 segundos antes de aparecer
    time.sleep(10)
    print("¡El lobo ha llegado!")
    # Rompe la barrera para capturar a las ovejas que no hayan cruzado
    barrera.reset()


# Crear y empezar los hilos de las ovejas
hilos = []
for i in range(NUM_OVELAS):
    hilo = threading.Thread(target=oveja, args=(i + 1,))
    hilos.append(hilo)
    hilo.start()
    time.sleep(1)  # Espaciado para simular llegada de ovejas

# Crear y empezar el hilo del lobo
hilo_lobo = threading.Thread(target=lobo)
hilo_lobo.start()

# Esperar a que todos los hilos de ovejas terminen
for hilo in hilos:
    hilo.join()

hilo_lobo.join()
print("Todas las ovejas han cruzado o han sido capturadas por el lobo.")
