"""
El módulo subprocess en Python permite la ejecución de comandos del sistema operativo y la interacción ç
con ellos desde un script.
Es particularmente útil para automatizar tareas que normalmente realizarías en la terminal o consola.
"""
import subprocess


# 1. Ejemplo de subprocess.run() en Windows (similar a ejecutar un comando en cmd)
result = subprocess.run(['dir'], capture_output=True, text=True, shell=True)

"""Python crea un nuevo proceso de shell y pasa el comando que deseas ejecutar como un string. 
Esto permite que el sistema interprete el comando como lo haría si lo ingresaras directamente 
en una terminal."""
print("Salida del comando 'dir':")
print(result.stdout)  # Muestra la salida del comando

"""
Parámetros importantes:
    args: Es una lista o cadena que especifica el comando y sus argumentos.
    capture_output: Captura la salida estándar y los errores (similar a stdout=subprocess.PIPE y stderr=subprocess.PIPE).
    text: Si es True, convierte los datos de salida y error en cadenas en lugar de bytes.
    check: Si es True, lanza una excepción si el proceso devuelve un código de salida diferente de cero.
    stdin= indica que le vamos a mandar un input (mirar ultimo ejemplo, es con .Pope pero un tb lo tiene)
    stdout=indica hacia donde va a ir el flujo de salida, puede ser una variable, un fichero, etc
Retorna: Un objeto CompletedProcess con atributos como:
    args: Comando ejecutado.
    returncode: Código de retorno del comando (0 significa éxito).
    stdout: Resultado estándar del comando.
    stderr: Mensajes de error.
"""


"""
La estructura que va dentro de los corchetes [] en subprocess.run() representa el comando y sus argumentos que deseas 
ejecutar en la terminal o shell.
Estructura general:
subprocess.run([comando, argumento1, argumento2, ...], shell=True)//crea una lista
comando: Es el nombre del programa o comando del sistema que quieres ejecutar, como ping, dir, ls, python, etc.
argumentos: Son los parámetros opcionales que le pasas al comando para modificar su comportamiento, como una dirección,
 una opción, o una ruta de archivo.

¿Por qué usar una lista?

La razón por la que Python usa una lista es para separar el comando principal de sus argumentos, lo que permite 
que Python gestione estos elementos de manera segura, sin tener que preocuparse por la interpretación especial 
que algunos caracteres podrían tener en una shell.
Ejemplo con varios argumentos

Si el comando tiene varios argumentos, simplemente añades más elementos a la lista. Por ejemplo:
subprocess.run(['ping', '-c', '4', 'google.com'], shell=True)


"""

# 2. Ejemplo de subprocess.Popen() en Windows
process = subprocess.Popen(['ping', 'google.com'], stdout=subprocess.PIPE, text=True)
for line in process.stdout:
    print(line, end='')  # Muestra cada línea de la salida de ping

"""
Parámetros importantes:
    stdin, stdout, stderr: Se utilizan para redirigir las entradas y salidas estándar.
    shell: Si es True, ejecuta el comando dentro de una shell.
Métodos del objeto Popen:
    communicate(): Espera a que el proceso termine y lee la entrada/salida.
    wait(): Espera a que el proceso termine.
    poll(): Verifica si el proceso ha terminado sin bloquear el programa.
"""


# 3. Ejemplo de subprocess.call() en Windows
return_code = subprocess.call(['ping', 'google.com', '-n', '2'], shell=True)  # -n 2 para solo 2 pings
print(f"El código de retorno es: {return_code}")

# 4. Ejemplo de subprocess.check_call() en Windows
try:
    subprocess.check_call(['ping', 'google.com', '-n', '2'], shell=True)
    print("Comando ejecutado correctamente.")
except subprocess.CalledProcessError as e:
    print(f"El comando falló con el código de error: {e.returncode}")
# 5. Ejemplo de subprocess.check_output() en Windows
try:
    output = subprocess.check_output(['ping', 'google.com', '-n', '2'], text=True, shell=True)
    print("Salida del comando check_output:")
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# 6. Ejemplo de redirección de salida a un archivo en Windows
with open('salida_dir.txt', 'w') as f:
    subprocess.run(['dir'], stdout=f, text=True, shell=True)
print("La salida del comando 'dir' se ha guardado en 'salida_dir.txt'.")

# 7. Ejemplo de encadenar comandos con pipes en Windows
p1 = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True, text=True)
p2 = subprocess.Popen(['findstr', '.py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True, shell=True)
p1.stdout.close()  # Cierra la salida del primer comando
output = p2.communicate()[0]
print("Archivos .py encontrados:")
print(output)

# Igual pero con .run()

print("CON RUN ------------")

# Ejecutar el primer comando y capturar la salida
p1 = subprocess.run(['dir'], capture_output=True, text=True, shell=True)

# Usar la salida del primer comando como entrada para el segundo comando
p2 = subprocess.run(['findstr', '.py'], input=p1.stdout, capture_output=True, text=True, shell=True)

# Imprimir el resultado
print("Archivos .py encontrados:")
print(p2.stdout)


# 8. Ejemplo con manejo de timeout y errores
try:
    result = subprocess.run(
        ['ping', 'google.com', '-n', '4'],  # Comando de 4 pings
        capture_output=True,
        text=True,
        timeout=10,  # Tiempo máximo de espera en segundos
        shell=True
    )
    print("Salida del comando con timeout:")
    print(result.stdout)
except subprocess.TimeoutExpired:
    print("El comando tardó demasiado y fue terminado.")
