import socket

# Crear el socket del servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 65434))
servidor.listen(1)
print("Servidor de chat iniciado en 127.0.0.1:65434")

# Esperar una conexión
conexion, direccion = servidor.accept()
print(f"Cliente conectado desde {direccion}")

while True:
    mensaje = conexion.recv(1024).decode('utf-8')
    if not mensaje or mensaje.lower() == "salir":
        print("El cliente ha cerrado la conexión.")
        break
    print(f"Cliente: {mensaje}")
    respuesta = input("Tú: ")
    conexion.sendall(respuesta.encode('utf-8'))

conexion.close()
servidor.close()
