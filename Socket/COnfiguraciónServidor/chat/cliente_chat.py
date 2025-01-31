import socket

# Crear el socket del cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 65434))
print("Conectado al servidor de chat.")

while True:
    mensaje = input("Tú: ")
    cliente.sendall(mensaje.encode('utf-8'))
    if mensaje.lower() == "salir":
        print("Cerrando conexión...")
        break
    respuesta = cliente.recv(1024).decode('utf-8')
    print(f"Servidor: {respuesta}")

cliente.close()
