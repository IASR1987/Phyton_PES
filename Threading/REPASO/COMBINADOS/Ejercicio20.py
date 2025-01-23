"""
Ejercicio 20: Línea de Ensamblaje de una Fábrica de Dispositivos
Contexto: En una línea de ensamblaje de una fábrica de dispositivos,
los productos pasan por varias etapas antes de estar completamente
ensamblados. Un producto pasa por montaje, revisión de calidad, y
empaquetado antes de poder ser almacenado.
Objetivo:
Implementar un sistema en el que cada producto pase por varias etapas
de producción de manera secuencial.
Usar Semaphore para controlar la capacidad del almacén de productos terminados.
Usar Condition para coordinar las etapas de producción y garantizar
que cada etapa se complete antes de que el producto pase a la siguiente.
Requisitos de implementación:
Los productos deben avanzar secuencialmente por cada etapa de producción.
La línea de ensamblaje solo puede almacenar un número limitado de
productos completamente terminados en el almacén.
Clases y herramientas recomendadas:
Semaphore y Condition.
"""
import threading
import time


# Capacidad del almacén
almacen = threading.Semaphore(0)

# Condiciones para las etapas de montaje y revisión
montaje = threading.Condition()
piezaMontada = False

revision = threading.Condition()
piezaRevisada = False

contador = 0

# Función para la primera etapa (montaje)
def primeraEtapa(id):
    global piezaMontada
    global contador
    print(f"Pieza {id} llega a la fábrica")
    with montaje:
        while piezaMontada:  # Si hay una pieza montada, espera
            montaje.wait()
        piezaMontada = True
        print(f"Pieza {id} montandose")
        time.sleep(2)
        print(f"Pieza {id} termina su montaje")
        piezaMontada = False
        montaje.notify_all()  # Notifica a la siguiente etapa

# Función para la segunda etapa (revisión de calidad)
def segundaEtapa(id):
    global piezaRevisada
    print(f"Pieza {id} llega a la segunda etapa (revisión)")
    with revision:
        while piezaRevisada:  # Si la pieza ya está revisada, espera
            revision.wait()
        piezaRevisada = True
        print(f"Pieza {id} revisandose")
        time.sleep(2)
        print(f"Pieza {id} termina su revisión")
        piezaRevisada = False
        revision.notify_all()  # Notifica que la revisión está lista

def almacenaje(id):
    global contador
    print(f"pieza{id} espera ser colocada en almacen")
    time.sleep(1)
    while contador < 5:
        almacen.acquire()
        print(f"Pieza {id} almacenada")
        contador += 1
        print(f"piezas en almacen " + str(contador))


# Función de producción para un hilo (montaje y revisión de una pieza)
def produccion(id):
    primeraEtapa(id)  # Paso 1: Montaje
    print(f"PIEZA {id} termina la primera etapa (montaje)")
    segundaEtapa(id)  # Paso 2: Revisión
    print(f"Pieza {id} completa todo el proceso")
    print(f"Pieza {id} va al almacen")
    almacenaje(id)

productos = []
for i in range(5):  # Simula la producción de 5 piezas
    producto = threading.Thread(target=produccion, args=(i + 1,))
    producto.start()
    productos.append(producto)

# Esperar que todos los hilos terminen
for producto in productos:
    producto.join()

print("Toda la producción ha finalizado.")

