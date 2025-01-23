"""
Ejercicio 22: Juego en Equipo - Sala de Escape
Contexto: En una sala de escape, un grupo de jugadores debe
resolver una serie de desafíos y avanzar juntos a la siguiente
sala. Cada sala tiene un punto de control que solo se puede superar
cuando todos los jugadores han completado la prueba.
Objetivo:
Usar Barrier para que todos los jugadores deban completar cada desafío
antes de avanzar al siguiente punto de control.
Usar Event para dar pistas en momentos específicos.
Usar Condition para permitir que los jugadores pidan ayuda solo cuando están atascados en una prueba.
Requisitos de implementación:
Cada jugador debe esperar a los demás en los puntos de control.
Las pistas solo deben aparecer cuando el evento esté activo.
Los jugadores solo pueden pedir ayuda cuando están bloqueados, y el sistema
debe responder solo si al menos la mitad de los jugadores están pidiendo ayuda.
Clases y herramientas recomendadas:
Barrier, Event, y Condition.
"""
import random
import threading
import time

#numero de jugadores
numero_jugadores = 5

#primera prueba
puntoControl1= threading.Barrier(numero_jugadores)
#segunda prueba
puntoControl2 = threading.Barrier(numero_jugadores)

#pistas
pista = threading.Event()

#condicion
condicion= threading.Condition()

#contador
contador=0
contador1=0

# Lock para proteger los contadores
lock = threading.Lock()


def p_C_1(id):
    global contador
    #jugadores afrontan la primera parte del juego
    time.sleep(1)
    #aleatorio para que necesiten pista
    bloqueo = random.randint(0,8)

    if bloqueo >=6:
        with condicion:
            with lock:
                # Contamos jugadores que necesitan pista
                contador += 1
            print(f"jugador {id} no es capaz de resolver el primer acertijo")
            print(f"jugador {id} bloqueado esperando a una pista")

            #devuelve true si es devuelto por un notify
            if condicion.wait(timeout=10):#timeout por si no llega a la mitad de jugadores
                pista.wait()
                print(f"jugador {id} recibimos la pista")
            else:
                #false al ser timeout
                print(f" jugador{id} tus compañeros te abandonan pasaras por pena")

    print(f"jugador {id} resuelve el primer acertijo, espera a sus compañeros")
    puntoControl1.wait()#barrera
    print(f"jugador {id} pasa a segundo punto de control")


def p_C_2(id):
    global contador1
    #jugadores afrontan la segunda parte del juego
    time.sleep(1)
    #aleatorio para que necesiten pista
    bloqueo = random.randint(0,8)

    #si el bloqueo es mayor o igual a 6
    if bloqueo >=6:
        with condicion:
            with lock:
                # Contamos jugadores que necesitan pista
                contador1 += 1
            print(f"jugador {id} no es capaz de resolver el segundo acertijo")
            print(f"jugador {id} bloqueado esperando a una pista")

            #devuelve true si es devuelto por un notify
            if condicion.wait(timeout=10):#tiempo de espera para sí hay menos de la mitad de jugadores sigue le flujo
                pista.wait()
                print(f"jugador {id} recibimos la pista")
            else:
                #false al ser timeout
                print(f" jugador{id} tus compañeros te abandonan pasaras por pena")

    print(f"jugador {id} resuelve el segundo acertijo, espera a sus compañeros")
    puntoControl2.wait()
    print(f"jugador {id} nos vamos a tomar una cervecita por lo bien que lo hemos hecho")


def controlContador():
    global contador,contador1
    while True:
        with lock:
            if contador > numero_jugadores / 2 or contador1 > numero_jugadores / 2:
                with condicion:
                    condicion.notify_all()


c = threading.Thread(target=controlContador, daemon=True)
c.start()


def juego(id):
    global contador
    p_C_1(id)
    p_C_2(id)

def pistas():
    while True:
        pista.set()
        time.sleep(random.randint(1,2))
        pista.clear()


#hilo ayudas
ayuda= threading.Thread(target=pistas, daemon=True)
ayuda.start()

jugadores = []

for i in range(numero_jugadores):
    jugador = threading.Thread(target=juego, args=(i+1,))
    jugador.start()
    jugadores.append(jugador)

for jugador in jugadores:
    jugador.join()


print("juego terminado en 'La Prensa' esta pagada la primera ronda, Güena gente")
