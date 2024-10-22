"""
Enunciado:
Escribe un programa que calcule el área de un círculo
a partir de su radio. Usa la fórmula:
Área = π * radio^2
(Usa math.pi para el valor de π)
"""
import math



radio=float(input("Introduce el radio del círculo"))

Area= math.pi*radio**2#dos asteriscos es potencia el número indica cuadrado, cubo etv

print("el área es ", Area)