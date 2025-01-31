import socket
import threading

def manejar_cliente(conexion, direccion):
    print(f"Nueva conexión desde {direccion}")
    while True:
        mensaje = conexion.recv(1024)
        if not mensaje:
            break
        print(f"Cliente {direccion}: {mensaje.decode('utf-8')}")
        conexion.sendall(b"Mensaje recibido")
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


# Cerrar conexión
conexion.close()
servidor.close()
