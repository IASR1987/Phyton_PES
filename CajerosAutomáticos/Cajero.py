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

class CuentaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, cantidad):
        if self.saldo<self.saldo-cantidad:
            print('saldo insuficiente')
        else:
            self.saldo -= cantidad


c1 = CuentaBancaria(100)
c2=CuentaBancaria(1)

