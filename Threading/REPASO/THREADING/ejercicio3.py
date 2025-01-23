"""
Ejercicio 3: Crear hilos que ejecuten diferentes tareas
Crea 3 hilos, cada uno ejecutando una función diferente:
uno calcula el cuadrado de un número dado, otro calcula
el cubo, y el tercero imprime si el número es par o impar.
Ejecuta estos hilos para el número 10
"""
import threading

numero=10

def cuadrado(numero):
    numero= numero*numero
    print(f"el cuadrado de 10 es {numero}.")

def cubo(numero):
    numero= numero*numero*numero
    print(f"el cubo de 10 es {numero}.")

def tercero(numero):
    if(numero%10==0):
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")

hilos=[]

for i in range(3):

    if(i==1):
        hilo= threading.Thread(target=cuadrado,args=(numero,))
        hilos.append(hilo)
        hilo.start()
    elif (i==2):
        hilo= threading.Thread(target=cubo,args=(numero,))
        hilos.append(hilo)
        hilo.start()
    else:
        hilo= threading.Thread(target=tercero,args=(numero,))
        hilos.append(hilo)
        hilo.start()


