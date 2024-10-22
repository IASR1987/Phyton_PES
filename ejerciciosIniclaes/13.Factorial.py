"""Escribe un programa que calcule el factorial de un número dado por
el usuario. El factorial de n se define como el producto de todos los
números enteros positivos hasta n
"""
def factorial():

    print("introduce un numero")
    numero= int(input())

    n=1
    resultado=1

    while n<=numero:
        resultado=resultado*n
        n+=1

    print("el factorial de "+ str(numero) + " es "+ str(resultado) +".")

factorial()