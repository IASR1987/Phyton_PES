"""
Divide una lista de 100 números en dos mitades y haz que cada hilo
sume una mitad. Usa Lock para acumular la suma total en una variable compartida.
"""

import threading

lista =list(range(1,101))
sumaTotal=0
candado= threading.Lock()

def sumaNumeros(primero,ultimo):
    global sumaTotal

    sumaMedia= sum(lista[primero:ultimo])


    with candado:
        print(threading.current_thread().name)
        print(sumaMedia)
        print(sumaTotal)
        sumaTotal+=sumaMedia
        print(sumaTotal)

hilo1 = threading.Thread(target=sumaNumeros, name='hilo1', args=(1,50))
hilo2 = threading.Thread(target=sumaNumeros,name='hilo2' ,args=(51,100))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(lista)