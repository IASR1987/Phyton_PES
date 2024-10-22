"""
Anagrama
Escribe una función que determine si dos palabras son anagramas
(es decir, si están formadas por las mismas letras en diferente orden).
"""

frase1 = input("Introduce frase \n")
frase2 = input("Introduce frase \n")


#comparamos cadenas sorted

frase1 = sorted(frase1)
print(frase1)
frase2 = sorted(frase2)
print(frase2)

if frase1 == frase2:
    print("Es una anagrama")
else:
    print("No es una anagrama")

