# Importaciones necesarias
from random import randint, random, uniform, randrange, choice, choices, sample, shuffle
import secrets

# 1. Usando randint
print("Usando randint:")
for i in range(10):
    avance = randint(1, 10)  # Número entero aleatorio entre 1 y 10
    print(avance)

# 2. Usando random
print("\nUsando random:")
for i in range(10):
    avance = random()  # Número flotante aleatorio entre 0.0 y 1.0
    print(avance)

# 3. Usando uniform
print("\nUsando uniform:")
for i in range(10):
    avance = uniform(1, 10)  # Número flotante aleatorio entre 1 y 10
    print(avance)

# 4. Usando randrange
print("\nUsando randrange:")
for i in range(10):
    avance = randrange(1, 11, 2)  # Número entero aleatorio entre 1 y 10, saltando de 2 en 2
    print(avance)

# 5. Usando choice
print("\nUsando choice:")
opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    avance = choice(opciones)  # Elige un elemento aleatorio de la lista
    print(avance)

# 6. Usando choices
print("\nUsando choices:")
resultados = choices(opciones, k=10)  # Elige 10 elementos aleatorios con reemplazo
print(resultados)

# 7. Usando sample
print("\nUsando sample:")
resultados = sample(opciones, k=5)  # Elige 5 elementos aleatorios sin reemplazo
print(resultados)

# 8. Usando shuffle
print("\nUsando shuffle:")
shuffle(opciones)  # Mezcla los elementos de la lista
print(opciones)

# 9. Usando secrets
print("\nUsando secrets:")
for i in range(10):
    avance = secrets.randbelow(10) + 1  # Número entero aleatorio seguro entre 1 y 10
    print(avance)


