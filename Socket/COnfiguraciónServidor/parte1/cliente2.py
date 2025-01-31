import socket

# Conectar al servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 65432))  # Dirección y puerto del servidor

print("Conectado al servidor. Escribe un mensaje para enviar.")
try:
    while True:
        mensaje = input("Tú: ")  # Ingresar mensaje
        if mensaje.lower() == "salir":
            print("Cerrando conexión.")
            break
        cliente.sendall(mensaje.encode('utf-8'))
        respuesta = cliente.recv(1024)
        print(f"Servidor2: {respuesta.decode('utf-8')}")
except:
    print("Conexión cerrada.")
finally:
    cliente.close()
