"""
Contador de Palabras

Escribe una función que cuente cuántas veces aparece
cada palabra en un texto dado, ignorando mayúsculas y puntuación.
"""

texto= "ismael angel soria rivero ismael"

texto = texto.replace('.', ' ').replace(',', ' ')

texto=texto.split()

texto = sorted(texto)

print(texto)


#creamos el diccionario
contador = {}

#recorremos el texto
for palabra in texto:
    #get busca las veces que aparece una palabra
    contador[palabra] = contador.get(palabra, 0) + 1
    #asigna la clave = se asigna el valor .get busca si existe una clave y da su valor.
    # al no estar daría 0 y le sumamos una de edte modo se crear clave palabra valor 1
    # en otro caso daría clave palabra valor las veces que hubiera aprecido


print(contador)
