import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)

print("Nombre del equipo " + host)
print("direccion Ip " + ip)


