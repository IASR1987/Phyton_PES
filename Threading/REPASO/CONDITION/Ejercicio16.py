"""
Ejercicio 16: Cola de mensajes entre productores y consumidores
Usa Condition para crear una cola de mensajes donde los productores
puedan colocar mensajes y los consumidores puedan retirarlos. La cola
debe permitir que varios productores y consumidores trabajen sin interferencias.
"""
import threading

#condicion es que la cola sea 5, ya que no se pueden meter más cosas en ellas
cola = threading.Condition()
