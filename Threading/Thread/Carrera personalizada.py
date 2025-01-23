
import random
import threading
import time  # Importar time desde el módulo estándar

fin_carrera = False
Amarillo = "\33[1;33m"
Reset = "\033[0m"  # Restablece el color al valor predeterminado



def corredor(emoji):
    camino = 0
    global fin_carrera

    while camino < 50 and not fin_carrera:
        avance = random.randint(1, 16)  # Calcular el avance en cada iteración
        camino += avance
        time.sleep(1)  # Simular tiempo de avance
        print("_" * camino + emoji+" ---> "+threading.current_thread().name) # nombre del hilo



        # Verificar si ha ganado
        if camino >= 50:
            fin_carrera = True
            print(f"{Amarillo}Victoria {emoji}{Reset}")



# Crear hilos para cada corredor
t = threading.Thread(target=corredor, args=["🐎"], name=["Caballo"])  # Caballo
t2 = threading.Thread(target=corredor, args=["🚜"], name=["Tractor"])  # Tractor
t3 = threading.Thread(target=corredor, args=["🏃‍♂️"], name=["Persona"])  # Persona corriendo

# Iniciar los hilos
t.start()
t2.start()
t3.start()