
#-1: Invierte la cadena.
cadena = "hola"
cadena_invertida = cadena[::-1]
print(cadena_invertida)  # Salida: "aloh"


#siempre toma el primer caracter y el diguiente dpenderá del numero dado
#-2: Toma cada segundo carácter de la cadena, comenzando desde el final.
#   a   l   o   h
#   1   2   3   4
#da el primer carcater de la cadena a y despues el 3 que es o
cadena = "hola"
cadena_invertida = cadena[::-2]
print(cadena_invertida)  # Salida: "ao" (toma 'a' y 'o')

#-3: Toma cada tercer carácter de la cadena, comenzando desde el final
cadena = "hola"
cadena_invertida = cadena[::-3]
print(cadena_invertida)  # Salida: "ah" (toma 'a' y 'h')

#-6
cadena = "abcdefg"
cadena_invertida = cadena[::-6]
print(cadena_invertida)  # Salida: "ga" (toma 'g' y 'a')

