from fastapi import FastAPI
from typing import List, Dict
from app.routers import producto
import uvicorn

app = FastAPI()

app.include_router(producto.router)


@app.get('/')
def home():
    return {"Fonoma": "Prueba para Desarrolladores Backend"}

