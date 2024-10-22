import re
import subprocess

while True:
    print("\n1. Entrar navegador")
    print("2. Abrir Notepad")
    print("3. Abrir programa")
    print("4. Abrir página web concreta")
    print("5. Abrir archivo concreto con Notepad")
    print("6. Salir")

    opcion = int(input("Introduce opción: "))

    if opcion == 1:
        try:
            url = "https://www.google.com"
            subprocess.run(['start',url],shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")

    elif opcion == 2:
        try:

            subprocess.run(['Notepad.exe'])

        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")

    elif opcion == 3:
        ruta = input("Introduce ruta del programa: ")
        try:
            subprocess.run([ruta])
        except FileNotFoundError:
            print(f"El archivo '{ruta}' no se encontró.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")

    elif opcion == 4:
        url = input("Introduce la URL de la página web: ")
        url='https://'+url
        rutaNavegador=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        try:
            subprocess.run([rutaNavegador,url], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")

    elif opcion == 5:

        print("1. buscar archivo por ruta")
        print("2. listar directorio")
        op = input("Introduce opcion: ")

        match op:
            case "1":
                archivo = input("Introduce ruta del archivo para abrir con Notepad: ")
                try:
                    subprocess.run(["Notepad.exe", archivo], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e.output}")

            case "2":
                print("Listar directorio")
                directorio="C:/Users/Ismael/ISMAEL_CICLO_SUPERIOR/SEGUNDO DAM/PSP/archivos/"
                try:
                    resultado = subprocess.run(["dir", directorio], shell=True, capture_output=True, text=True)
                    # Filtrar los archivos que terminan en .txt
                    # Filtrar solo los archivos .txt y extraer sus nombres
                    archivos_txt = re.findall(r'\b\w+\.txt\b', resultado.stdout)
                    # r' se usa para que las barras invertidas (\) se tratan literalmente, sin necesidad de escape adicional
                    # \b Este es un límite de palabra. Indica que el patrón que sigue debe estar al principio o al final de una palabra.
                    # \w+: Coincide con cualquier carácter alfanumérico, incluye culquier caracter, el + indica que habra varios
                    # \.text significa que estamos buscando un punto literal. => en este caso .text
                    # \b límite de palabra que asegura que lo que viene después de .txt no sea parte de otra palabra file.txt123(no valdría)

                    print(archivos_txt)

                    archivo = input("elige el fichero")
                    archivo=directorio+archivo
                    subprocess.run(["Notepad.exe",archivo], check=True)

                except subprocess.CalledProcessError as e:
                    print(f"Error: {e.output}")
    elif opcion == 6:
        print("Saliendo del programa.")
        break  # Salir del bucle y finalizar el programa

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
