"""
Contar vocales en una cadena

Enunciado:
Crea un programa que cuente cuántas vocales hay en una cadena introducida por el usuario.
"""

frase=input("Introdcue una frase \n")
vocales=0

for letra in frase:
    if letra in "aeiouAEIOU":
        vocales+=1

print("el número de vocales es",vocales)

def es_vocal(letra):
    return letra.lower() in "aeiou"

frase = input("Introduce una frase: ")
contador_vocales = 0

# Recorremos cada letra de la frase
for letra in frase:
    if es_vocal(letra):
        contador_vocales += 1

print(f"La frase contiene {contador_vocales} vocales.")
