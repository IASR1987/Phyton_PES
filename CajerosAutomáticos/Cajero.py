"""
Ejercicio: Cajero automático multihilo con Lock
Contexto:
En un banco, múltiples cajeros automáticos permiten a los clientes retirar dinero
de sus cuentas. Todos los cajeros están conectados a la misma cuenta bancaria y
pueden ser utilizados simultáneamente por varios clientes. Sin embargo, si varios
cajeros intentan realizar operaciones sobre la misma cuenta al mismo tiempo sin control,
podrían surgir inconsistencias en el saldo (por ejemplo, un saldo negativo o retiros erróneos).
Tu tarea es simular este escenario usando hilos en Python y controlar el acceso concurrente
a la cuenta bancaria. Cada cajero será representado por un hilo que intentará retirar dinero
de la misma cuenta. Evita que varios cajeros retiren dinero al mismo tiempo y causen problemas
de consistencia.
Objetivos:
Crear una clase CuentaBancaria que gestione el saldo de la cuenta y permita realizar retiros.
Implementar el metodo retirar(cantidad) en la clase CuentaBancaria para que los retiros se
realicen de forma segura.
Simular varios hilos (cajeros) que intenten retirar dinero simultáneamente de la misma cuenta.
Mostrar el saldo antes y después de cada operación, indicando si el retiro fue exitoso o si no
había suficiente dinero en la cuenta.
Requisitos:
Implementa una clase CuentaBancaria con un saldo inicial.
Cada hilo (cajero) intentará retirar una cantidad de dinero aleatoria entre 10 y 100 unidades.
Imprime mensajes que indiquen qué cajero (hilo) está intentando retirar dinero, si la operación
fue exitosa y el saldo restante.
Imprime un mensaje cuando un cajero no puede realizar el retiro porque no hay suficiente dinero.

"""
import threading
import time

candado=threading.Lock()

class CuentaBancaria():
    def __init__(self,):
        self.saldo = 1000

    def retirar(self, cantidad):
        with candado:
            if self.saldo<self.saldo-cantidad:
                print('saldo insuficiente')
            else:
                self.saldo -= cantidad
                print('saldo Actual '+str(self.saldo))
                time.sleep(2)

    def ingresar(self, cantidad):
        with candado:
            self.saldo += cantidad
            print('saldo Actual ' + str(self.saldo))
            time.sleep(2)
hilos=[]
cuenta= CuentaBancaria()

for i in range(10):
    if i%2==0:
        hilo=threading.Thread(target=cuenta.retirar, args=(100,))
        hilos.append(hilo)
    else:
        hilo=threading.Thread(target=cuenta.ingresar, args=(200,))
        hilos.append(hilo)

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print(cuenta.saldo)