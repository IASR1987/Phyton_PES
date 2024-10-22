import random
from random import randint

numero=random.randint(1,100)
print(numero)
correcto = bool = False

while not correcto:  # Simula el "do"
    numeroUsuario = int(input("Introduce tu predicción\n"))

    if numero == numeroUsuario:
        print("¡Números iguales!")
        correcto=True
        #break  # Rompe el bucle si la condición es verdadera
    else:
        print("El número distintos.")

while True:
    numeroUsuario = int(input("Introduce tu predicción\n"))

    if numero == numeroUsuario:
        print("¡Números iguales!")
        break  # Rompe el bucle si la condición es verdadera
    else:
        print("El número distintos.")