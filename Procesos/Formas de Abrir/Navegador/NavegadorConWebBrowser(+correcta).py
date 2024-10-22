import webbrowser

url = input("Ingrese la url del web que desea buscar: ")

# Verificar si la URL comienza con 'http://' o 'https://'
if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url  # Agrega 'http://' si no está presente

webbrowser.open(url)
