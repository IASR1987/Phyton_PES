
def CadenaLarga(cadena):
    contador={}
    longitudMayor=0
    longitud=0

    for letra in cadena:
        contador[letra]=contador.get(letra,0)+1
        if contador.get(letra)==1:
            longitud+=1
        else:
            if longitud>longitudMayor:
                longitudMayor=longitud
            contador = {letra: 1}  # Reiniciar el contador con la letra actual para que no perdamos una letra de la cadena
            longitud = 1  # Reiniciar longitud a 1 para la letra actual

    if longitud > longitudMayor:
        longitudMayor = longitud  # Verifica la última longitud

    return longitudMayor

print(CadenaLarga("cadenaaaaaa"))