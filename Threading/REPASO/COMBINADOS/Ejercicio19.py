"""
Ejercicio 19: Simulación de un Aeropuerto con Control de Pistas y Retrasos
Contexto: En un aeropuerto, los aviones necesitan coordinarse para despegar
y aterrizar sin interferencias. Este aeropuerto tiene solo dos pistas, y
cada avión debe realizar mantenimiento previo al vuelo antes de despegar.
Además, puede haber retrasos causados por malas condiciones climáticas,
durante los cuales ningún avión puede despegar.
Objetivo:
Simular varios aviones (hilos) que desean despegar o aterrizar.
Controlar el acceso a las pistas usando un Semaphore para permitir
que un máximo de dos aviones ocupen las pistas a la vez.
Usar un Barrier para simular que todos los aviones deben pasar por mantenimiento antes de poder despegar.
Usar un Event para activar y desactivar retrasos de despegue debido a condiciones climáticas.
Requisitos de implementación:
Los aviones deben esperar a que una pista esté disponible antes de despegar o aterrizar.
Los aviones deben pasar por mantenimiento antes de poder despegar.
Si el evento de retraso climático está activo, los aviones deben esperar hasta que el clima mejore para poder despegar.
Clases y herramientas recomendadas:
Semaphore, Barrier, y Event.
"""
import threading
import time

#controlamos el acceso a la pista
accesoPistas=threading.Semaphore(2)

mantenimiento = threading.Barrier(2)

climatologia= threading.Event()

contador=3

def procesoDespegue(id):
    global contador
    print(f"Avion {id} se encuentra en el aeropuerto")
    accesoPistas.acquire()
    print(f"Avion {id} entra en la pista")
    #el avion debe hacer su mantenimiento debe haber dos aviones=> barrera
    try:
        mantenimiento.wait(timeout=5)
        time.sleep(6) #tiempo de mantenimiento
        print(f"avion{id} dispuesta a despegar observaremos el tiempo")
        climatologia.wait()
        print(f"avion {id} está despegando")
        #despega el avion => sale de la pista
        accesoPistas.release()
    except Exception as e:
        print(f"El avion {id}  no puede despegar solo, asi que vuelve a su hangar")

def clima():
    while True:
        # intercalaremos borrasca y buen tiempo
        print("Borrasca y lluvia imposible el despegue")
        time.sleep(10)
        climatologia.set()
        print("Tiempo bueno aviones pueden despegar")
        time.sleep(10)
        climatologia.clear()


Aviones = []

#iniciar el clima
Tiempo= threading.Thread(target=clima, daemon=True)
Tiempo.start()

for i in range(contador):
    avion=threading.Thread(target=procesoDespegue, args=(i+1,))
    Aviones.append(avion)
    avion.start()

for i in range(contador):
    Aviones[i].join()

