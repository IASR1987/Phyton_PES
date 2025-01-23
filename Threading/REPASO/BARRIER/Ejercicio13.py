"""
Ejercicio 13: Coordinación de un grupo en puntos de control
Usa Barrier para simular un grupo de excursionistas que debe
llegar a puntos de control a la vez. Crea 5 excursionistas que
deben esperar en cada punto de control (barrera) hasta que todos
lleguen, antes de avanzar al siguiente punto.
"""
import random
import threading
import time

puntoControl = threading.Barrier(5)
puntoControl2 = threading.Barrier(5)
puntoControl3 = threading.Barrier(5)
contador = 0

def pasarP1(id):
    global contador
    time.sleep(random.randint(3,6))
    print(f"Excursionista{id} acaba de llegar al primer punto de control")
    puntoControl.wait()
    contador += 1


def pasarP2(id):
    global contador
    time.sleep(random.randint(3,6))
    print(f"Excursionista{id} acaba de llegar al segundo punto de control")
    puntoControl2.wait()
    contador += 1

def pasarP3(id):
    global contador
    time.sleep(random.randint(3,6))
    print(f"Excursionista{id} acaba de llegar al tercer punto de control")
    puntoControl3.wait()
    contador += 1

def excursion(id):
    pasarP1(id)
    if(contador == 5):
        print("continuamos al siguiente punto de control")
    pasarP2(id)
    if (contador == 10):
        print("continuamos al siguiente punto de control")
    pasarP3(id)
    time.sleep(2)
    if (contador==15):
        print("terminamos")


excursionistas=[]

for i in range(5):
    excursionista = threading.Thread(target=excursion, args=(i,))
    excursionista.start()
    excursionistas.append(excursionista)


for excursionista in excursionistas:
    excursionista.join()

