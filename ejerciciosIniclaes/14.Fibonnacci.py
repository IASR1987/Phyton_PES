"""
Escribe un programa que genere los primeros n números de la
secuencia de Fibonacci.
"""

def Fibo():
    print("Intoduce un número n")
    numero= int(input())

    a=0
    b=1
    c=0

    if numero==1:
        print(a)
    elif numero==2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for _ in range(3, numero + 1):
            c = a + b
            a = b
            b = c
            print(c)
    print("El número es " + str(c))  # Imprime el resultado final
Fibo()