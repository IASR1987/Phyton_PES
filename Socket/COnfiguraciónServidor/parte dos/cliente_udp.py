import socket

# Crear un socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar un mensaje al servidor
mensaje = "Hola, servidor UDP!"
cliente.sendto(mensaje.encode('utf-8'), ("127.0.0.1", 65433))

# Recibir respuesta del servidor
respuesta, direccion = cliente.recvfrom(1024)
print(f"Respuesta del servidor: {respuesta.decode('utf-8')}")

# Cerrar el socket
cliente.close()
