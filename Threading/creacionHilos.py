import threading
import time

"""Ejecución secuencial

def desayunar():
    print("Iniciando")
    time.sleep(2)
    print("Terminando")

def tomar_cafe():
    print("Iniciando")
    time.sleep(3)
    print("Terminando")

def estudiar():
    print("Iniciando")
    time.sleep(4)
    print("Terminando")

inicio = time.perf_counter()
desayunar()
tomar_cafe()
estudiar()

fin=time.perf_counter() - inicio

print(fin)

"""
"""ejecucion con hilos"""

def desayunar():
    print("Inicio desayuno")
    time.sleep(2)
    print("Termino de desayuna")

def tomar_cafe():
    print("Inico cafe")
    time.sleep(3)
    print("Termino cafe")

def estudiar():
    print("Inicio estudio")
    time.sleep(4)
    print("Termino estudio")



"""Creamos los hilos"""
hiloDesayunar= threading.Thread(target=desayunar, args=())
hiloCafe = threading.Thread(target=tomar_cafe, args=())
hiloEstudiar = threading.Thread(target=estudiar, args=())

inicio = time.perf_counter()
"""Inicializo los hilos"""
hiloDesayunar.start()
hiloCafe.start()
hiloEstudiar.start()


"""esperar que acaben los hilos para que el 
progrma principal continue"""
"""dino pusieramos el join el programa continuaría
y la frase ismael soria saldría antes de que terminaran los hilos"""
hiloDesayunar.join()
hiloCafe.join()
hiloEstudiar.join()

print("Ismael Soria")

fin=time.perf_counter() - inicio

print(fin)