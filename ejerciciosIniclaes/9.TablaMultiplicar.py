"""
Tabla de multiplicar

Enunciado:
Crea un programa que muestre la tabla de multiplicar de un número que el usuario ingrese.
"""

def tablaMultiplicar(a):
    for i in range(1,11):
        print(a," x ", i, " = ", a*i )

tablaMultiplicar(1)
tablaMultiplicar(2)