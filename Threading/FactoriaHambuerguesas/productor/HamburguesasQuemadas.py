import threading
import time

# Semáforos
semaforoC = threading.Semaphore(5)  # Máximo 5 cocineros trabajando simultáneamente
semaforoM = threading.Semaphore(0)  # No hay hamburguesas disponibles al principio (meseros esperan)
semaforoB = threading.Semaphore(5)  # Máximo 5 hamburguesas en la barra al mismo tiempo

# Lista para los hilos de cocineros y meseros
Cocineros = []
Meseros = []

# Función que simula el trabajo de los cocineros
def cocinero(id):
    semaforoC.acquire()  # El cocinero adquiere el semáforo (empieza a cocinar)
    print(f"Cocinero {id} cocinando Hamburguesa {id}.")
    time.sleep(1)  # Tiempo para cocinar la hamburguesa
    semaforoB.acquire()  # El cocinero coloca la hamburguesa en la barra (puede haber máximo 5 hamburguesas)
    print(f"Hamburguesa {id} en la barra.")
    semaforoM.release()  # Notifica a un mesero que puede tomar la hamburguesa
    semaforoC.release()  # Libera el espacio para que otro cocinero trabaje

# Función que simula el trabajo de los meseros
def mesero(id):
    semaforoM.acquire()  # El mesero espera que haya una hamburguesa disponible en la barra
    print(f"Camarero {id} coge la Hamburguesa {id}.")
    time.sleep(2)  # Tiempo para servir la hamburguesa
    print(f"Hamburguesa {id} servida por Camarero {id}.")
    semaforoB.release()  # Libera el espacio en la barra (permite que otro cocinero coloque una hamburguesa)

# Crear 10 cocineros y 10 meseros
for i in range(10):
    Cocineros.append(threading.Thread(target=cocinero, args=(i,)))
    Meseros.append(threading.Thread(target=mesero, args=(i,)))

# Iniciar los hilos de cocineros y meseros
for i in range(10):
    Cocineros[i].start()
    Meseros[i].start()

# Esperar a que todos los hilos terminen (en este caso los hilos no terminan porque los cocineros y meseros son infinitos)
# Para fines prácticos, esto no se usaría en producción, pero es útil para que el programa principal espere a que todo termine
for i in range(10):
    Cocineros[i].join()
    Meseros[i].join()

print("Todos los hilos han terminado.")
