"""
Ejercicio 7: Controlar la entrada a una sala limitada
Simula una sala de espera con capacidad limitada a 3
personas usando Semaphore. Cada vez que un hilo (persona)
entra en la sala, debe esperar 1-3 segundos. Imprime un
mensaje cuando una persona entra y sale de la sala.
"""
import random
import threading
import time

#limite de entrada
portero = threading.Semaphore(3)

def entrada(id):
    portero.acquire()
    #tiempo que está una persona en la discoteca
    print(f"Persona {id} ha entrado vamos a echar unos dancing")
    time.sleep(random.randint(5,10))
    print(f"Persona {id} pa casa que va perjudicada")
    portero.release()


personas=[]

numeroPersonas=10

for i in range(numeroPersonas):
    persona = threading.Thread(target=entrada, args=(i,))
    personas.append(persona)
    persona.start()

for persona in personas:
    persona.join()

print("cerramos la discoteca")