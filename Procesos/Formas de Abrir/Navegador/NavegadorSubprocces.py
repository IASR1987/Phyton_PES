import subprocess

# Ruta del navegador (en este caso Chrome)
#sino indicamos la ruta del navegdor abrirá el que tengamos puesto por defecto
ruta_navegador = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
url = 'https://www.google.com'

subprocess.run([ruta_navegador, url])


"""otra opcion menos seguras por el uso de shell=true"""

url = 'https://www.marca.com'
subprocess.run(['start', url], shell=True)
