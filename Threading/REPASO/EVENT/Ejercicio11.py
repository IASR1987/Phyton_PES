"""
Ejercicio 11: Sistema de alarma de seguridad
Crea un sistema donde varios sensores (hilos)
esperan una señal de alarma (Event). Cuando el
Event se activa (simulando que se ha activado la
alarma), todos los sensores deben imprimir un
mensaje de "Alarma activada". Controla la activación
y desactivación de la alarma con set() y clear() de Event.
"""
import random
import threading
import time

alarmaActivada=threading.Event()

def alarmAlarma(id):
    while True:
        time.sleep(1)
        print(f"Alarma {id} en funcionamiento")
        #alarma en espera
        alarmaActivada.wait()
        print(f"alarma {id} sonando")
        time.sleep(2)
        print(f"alarma {id} desactivada")

def robo():
    print("esperando que entren los ladrones")
    alarmaActivada.set()
    print("entran a robar")
    time.sleep(2)#tiempo que roban
    alarmaActivada.clear()
    print("Todo bajo control")

sensores=[]

for i in range(10):
    sensor = threading.Thread(target=alarmAlarma, args=(i,), daemon=True)
    sensor.start()
    sensores.append(sensor)

#tiempo para dejar alarmas puestas
time.sleep(2)
robar = threading.Thread(target=robo)
robar.start()

time.sleep(5)
print("Sistema de alarma finalizado a la espera de mas ladrones.")