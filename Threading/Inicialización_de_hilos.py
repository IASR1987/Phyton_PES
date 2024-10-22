import threading

# Definimos la función 'ejecutar'
def ejecutar(parametro1=10, parametro2=20):
    print(f'Hilo en ejecución: {threading.current_thread().name}')
    print(f'Parámetro 1: {parametro1}, Parámetro 2: {parametro2}')


# Creamos los hilos
hilo1 = threading.Thread(target=ejecutar)
hilo2 = threading.Thread(target=ejecutar, args=(100, 200))
hilo3 = threading.Thread(target=ejecutar, kwargs={'parametro1': 1000, 'parametro2': 2000})
hilo4 = threading.Thread(target=ejecutar, args=(300, 400), name='hilo4')

# Iniciamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

# Esperamos a que los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

print('Todos los hilos han finalizado.')
