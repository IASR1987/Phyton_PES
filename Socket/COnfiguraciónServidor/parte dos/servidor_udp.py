
import socket

# Crear un socket UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular el socket a una dirección y puerto
servidor.bind(("127.0.0.1", 65433))
print("Servidor UDP iniciado en 127.0.0.1:65433")

while True:
    mensaje, direccion = servidor.recvfrom(1024)
    print(f"Mensaje recibido de {direccion}: {mensaje.decode('utf-8')}")
    servidor.sendto(b"Mensaje recibido", direccion)
