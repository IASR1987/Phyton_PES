import socket
import threading
import random

def calcular_ganador(eleccion_cliente, eleccion_servidor):
    reglas = {
        "piedra": "tijeras",
        "papel": "piedra",
        "tijeras": "papel"
    }
    if eleccion_cliente == eleccion_servidor:
        return "Empate"
    elif reglas[eleccion_cliente] == eleccion_servidor:
        return "Ganaste"
    else:
        return "Perdiste"

def manejar_cliente(conexion, direccion):
    print(f"Conexión aceptada desde {direccion}")
    while True:
        try:
            # Recibir elección del cliente
            eleccion_cliente = conexion.recv(1024).decode('utf-8')
            if not eleccion_cliente:
                break

            print(f"El cliente {direccion} eligió: {eleccion_cliente}")

            # Generar elección del servidor
            eleccion_servidor = random.choice(["piedra", "papel", "tijeras"])
            print(f"El servidor eligió: {eleccion_servidor}")

            # Determinar el resultado
            resultado = calcular_ganador(eleccion_cliente, eleccion_servidor)
            mensaje_respuesta = f"Servidor eligió: {eleccion_servidor}. Resultado: {resultado}"

            # Enviar resultado al cliente
            conexion.sendall(mensaje_respuesta.encode('utf-8'))
        except:
            print(f"Conexión con {direccion} terminada.")
            break
    conexion.close()

# Configurar el servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 65432))
servidor.listen(5)
print("Servidor escuchando en 127.0.0.1:65432")

while True:
    conexion, direccion = servidor.accept()
    hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
    hilo.start()
