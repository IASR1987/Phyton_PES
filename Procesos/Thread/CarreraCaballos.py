import random
import threading
import time


carrera_terminada = False

def caballo():
    global carrera_terminada
    camino = 0
    while camino<50 and not carrera_terminada:
        avance=(int)(random.random()*10)
        camino+=avance
        time.sleep(0.2)
        print("." * camino + "🐎")
        time.sleep(2)
        if camino >= 50:
            carrera_terminada=True
            print("Victoria del potro salvaje")

def tractor():
    global carrera_terminada
    camino = 0
    while camino < 50 and not carrera_terminada:
        avance = (int)(random.random() * 10)
        camino += avance
        time.sleep(0.2)
        print("." * camino + "🚜")
        time.sleep(2)
        if camino >= 50:
            carrera_terminada = True
            print("Victoria del tractor")


camino2=0
t=threading.Thread(target=caballo)
t2=threading.Thread(target=tractor)
t.start()
t2.start()

while camino2 < 50 and not carrera_terminada:
        avance = (int)(random.random() * 10)
        camino2 += avance
        time.sleep(0.2)
        print("." * camino2 + "🏃‍♂️")
        time.sleep(2)

if camino2 >=50:
    carrera_terminada = True
    print("Victoria del muchacho intrépido")


