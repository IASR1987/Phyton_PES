import threading
import time



""" ejemplo sin hilo demonio
a pesar de que termine el programa principal 
el temporizador continua
def tiempo():
    print()
    print()
    contador=0
    while True:
        time.sleep(1)
        contador+=1
        print(contador, " Segundos")


hiloTiempo= threading.Thread(target=tiempo)
hiloTiempo.start()

print('Ismael')
"""

"""la ejecución del hilo demonio
comienza y se termina con la ejecucion del print ismael
que tiene puesto un time sleep de 4 segundos, ya que 
sino pasara esto el hilo demnio ni siquiera se ejecutaria"""

def tiempo():
    print()
    print()
    contador=0
    while True:
        time.sleep(1)
        contador+=1

        print(contador, " Segundos")


hiloTiempo= threading.Thread(target=tiempo, daemon=True)
hiloTiempo.start()

time.sleep(4)
print('Ismael')

