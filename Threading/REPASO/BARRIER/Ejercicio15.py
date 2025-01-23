"""
Ejercicio 15: Sincronización en un juego multijugador
Crea una simulación de un juego en línea donde 4 jugadores
deben esperar a que todos estén listos antes de comenzar la partida.
Usa Barrier para sincronizar a los jugadores, haciendo que cada
uno espere hasta que todos estén listos.
"""
import threading
import time

esperandoJugadores = threading.Barrier(4)
contador= 0

def jugar(id):
    global contador
    print(f"jugador{id} esperando a los compañeros")
    esperandoJugadores.wait()
    contador += 1
    if(contador%4==0):
        print(f"empieza la partida")
        time.sleep(3)


jugadores=[]

for i in range(40):
    jugador=threading.Thread(target=jugar, args=(i,))
    jugadores.append(jugador)
    jugador.start()

for j in jugadores:
    j.join()

