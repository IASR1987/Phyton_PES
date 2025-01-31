import socket

def mostrar_menu():
    print("Elige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("4. Salir")

# Conectar al servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("192.168.41.224", 65432))

try:
    while True:
        mostrar_menu()
        opcion = input("Tu elección: ")
        if opcion == "4":
            print("¡Gracias por jugar! Cerrando conexión.")
            break

        # Validar la entrada del usuario
        elecciones = {"1": "piedra", "2": "papel", "3": "tijeras"}
        eleccion = elecciones.get(opcion)
        if not eleccion:
            print("Opción inválida. Inténtalo de nuevo.")
            continue

        # Enviar elección al servidor
        cliente.sendall(eleccion.encode('utf-8'))

        # Recibir y mostrar el resultado
        resultado = cliente.recv(1024).decode('utf-8')
        print(resultado)
except:
    print("Se perdió la conexión con el servidor.")
finally:
    cliente.close()
