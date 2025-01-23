import random
import time
import threading

# Recursos compartidos
operarioCalidad = threading.Semaphore(3)  # Controla los operarios de calidad
operarioAlmacen = threading.Semaphore(3)  # Controla los operarios de almacén
condicion = threading.Condition()  # Para coordinar el acceso a la cinta
cinta = []
piezasBien = []
piezasMal = []
piezasPerdidas = []
piezasEmpaquetadas = []
finalizar = False  # Bandera para indicar que se deben detener los hilos


def fabricar(id_producto):
    global finalizar

    # Fase 1: Llegada de la pieza y revisión de calidad
    operarioCalidad.acquire()
    print(f"La pieza {id_producto} llega a la cinta.")
    time.sleep(3)  # Simula tiempo de fabricación

    with condicion:
        cinta.append(id_producto)
        print(f"La pieza {id_producto} se añadió a la cinta.")
        condicion.notify_all()  # Notificar que hay piezas en la cinta

    # Fase 2: Revisar la calidad
    with condicion:
        while len(cinta) == 0 and not finalizar:
            print(f"Operario de calidad espera piezas en la cinta...")
            condicion.wait()

        if finalizar and len(cinta) == 0:  # Salir si se finaliza el proceso
            operarioCalidad.release()
            return

        pieza = cinta.pop()
        print(f"La pieza {pieza} se está revisando.")
        if random.randint(1, 2) == 1:
            piezasBien.append(pieza)
            print(f"La pieza {pieza} está en buen estado.")
        else:
            piezasMal.append(pieza)
            print(f"La pieza {pieza} está defectuosa.")
        condicion.notify_all()  # Notificar que hay piezas revisadas
    operarioCalidad.release()

    # Fase 3: Empaquetar piezas buenas
    operarioAlmacen.acquire()
    with condicion:
        while len(piezasBien) == 0 and not finalizar:
            print(f"Operario de almacén espera piezas buenas...")
            condicion.wait()

        if finalizar and len(piezasBien) == 0:  # Salir si se finaliza el proceso
            operarioAlmacen.release()
            return

        pieza = piezasBien.pop()
        print(f"La pieza {pieza} se está empaquetando.")
        if random.randint(1, 3) == 1:
            piezasPerdidas.append(pieza)
            print(f"La pieza {pieza} se perdió en el proceso.")
        else:
            piezasEmpaquetadas.append(pieza)
            print(f"La pieza {pieza} fue empaquetada y enviada al almacén.")
        condicion.notify_all()  # Notificar que hay cambios en el almacén
    operarioAlmacen.release()


# Crear y lanzar hilos
stock = []
for i in range(10):
    pieza = threading.Thread(target=fabricar, args=(i + 1,))
    stock.append(pieza)
    pieza.start()
    time.sleep(0.2)  # Espaciado entre la llegada de las piezas

# Esperar a que todos los hilos terminen
for pieza in stock:
    pieza.join()

# Indicar que el proceso ha finalizado
with condicion:
    finalizar = True
    condicion.notify_all()  # Notificar a todos los hilos que deben terminar

# Resultados finales
print("\n=== Resultados Finales ===")
print(f"Numero de piezas bien: {len(piezasBien)}; {piezasBien}")
print(f"Numero de piezas mal: {len(piezasMal)}; {piezasMal}")
print(f"Numero de piezas empaquetadas: {len(piezasEmpaquetadas)}; {piezasEmpaquetadas}")
print(f"Numero de piezas perdidas: {len(piezasPerdidas)}; {piezasPerdidas}")