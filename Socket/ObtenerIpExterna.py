import socket

try:

    host = 'www.google.com'

    print("IP "+host+" : "+socket.gethostbyname(host))

except socket.gaierror:

    print("No se pudo resolver el host")
