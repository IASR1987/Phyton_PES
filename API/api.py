from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Instancia de FastAPI
app = FastAPI()

#ruta principal
@app.get("/hola")
def home():
    return{"mensaje": "Bienvenido a la Api de Productos"}


