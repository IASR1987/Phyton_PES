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
totalOvejas = 100
totalLobos=6
TAMANO_GRUPO = 3
contador=0

# Barrera que sincroniza a las ovejas en cada cruce
barrera = threading.Barrier(TAMANO_GRUPO)


def oveja(id):
    global contador
    time.sleep(random.randint(0, 15))
    print(f'oveja {id} cruza el valle')
    time.sleep(1)
    print(f'oveja {id} llega a la barrera')
    time.sleep(2)

    try:
        barrera.wait()
        print(f'oveja {id} se salva')
        contador=contador+1
        time.sleep(1)
    except threading.BrokenBarrierError:
        print(f"Devora a la Oveja {id}.")

def lobo():
    print('LOBO Llega un lobo a lo lejos')
    time.sleep(4)
    barrera.reset()
    print('LOBO llega a  la barrera')# Romper la barrera para simular el ataque del lobo

hilos_ovejas = []
for i in range(totalOvejas):
    hilo = threading.Thread(target=oveja, args=(i+1,))
    hilos_ovejas.append(hilo)
    hilo.start()


hilo_lobos=[]
for i in range(totalLobos):
    hilo = threading.Thread(target=lobo, daemon=True)
    hilo_lobos.append(hilo)
    hilo.start()
    time.sleep(5)


# Esperar a que todos los hilos de las ovejas terminen
for hilo in hilos_ovejas:
    hilo.join()

for hilo in hilo_lobos:
    hilo.join()

print('ovejas salvadas'+ str(contador))