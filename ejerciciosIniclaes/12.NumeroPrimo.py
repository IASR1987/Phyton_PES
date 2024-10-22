"""
Identifica si un número es primo o no
"""

numero=int(input("Introduce un número \n"))
EsPrimo = True

if numero>=2:
    for i in range(2, int(numero ** 0.5) + 1):#es la mitad del numero pero debe sumar uno para que lo incluya
        if numero % i == 0:# si el número
            EsPrimo = False
            break
else:
    EsPrimo = False


if(EsPrimo): print("El numero es primo")
else: print("El numero no es primo")