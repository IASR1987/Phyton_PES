"""
Escribe un programa que determine si una cadena es un palíndromo.
Una cadena es un palíndromo si se lee igual de izquierda a derecha
que de derecha a izquierda (ignorando espacios y
mayúsculas/minúsculas).
"""

print("introduce una palabra")
palabra = str(input())

numero = len(palabra)
print(numero)
resultado = True

contador=numero-1

#si le damos la vuelta
palabraVuelta = palabra[::-1]
print(palabraVuelta)

for i in range(0,numero):
    if palabra[i] != palabra[contador]:
        print(palabra[i],palabra[contador])
        resultado = False
        break
    contador-=1

if resultado:
    print("si")
else:
    print("no")


