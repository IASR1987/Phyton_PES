
import threading
import time

#numero que accede escenario
numero_personas_escenario=5

#numero de personas en el festival
aforo=15

#semaforo que controla el acceso
portero=threading.BoundedSemaphore(5)

#evento que controla la música
musica=threading.Event()


def Escenario(id):
    print(f"Espectador {id} quiere entrar en el escenario")
    # haya aforo disponible
    portero.acquire()
    musica.wait()
    print(f"Espectador {id}  entra en el escenario")

    time.sleep(2)
    if not musica.is_set():
        portero.release()
        print(f"Espectador {id} abandona el recinto.")


def RuidoAmbiental():
    while True:
        print("MÚSICA VIVO")
        musica.set()
        #tiempo aleatorio de baile
        time.sleep(2)
        musica.clear()
        print("MUSICA PARADA")
        print("preparando concierto")
        time.sleep(2)


tecnicoSonido= threading.Thread(target= RuidoAmbiental, daemon=True)
tecnicoSonido.start()

Publico = []

for i in range(aforo):
    persona= threading.Thread(target=Escenario, args=(i,))
    persona.start()
    Publico.append(persona)

for persona in Publico:
    persona.join()

print("FESTIVAL CERRADO")