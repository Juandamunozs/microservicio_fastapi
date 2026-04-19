from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import controllerStock, controllerStats
from database.database import init_db
from service.serviceStock import NotFoundError, ConflictError
from utils.exception_handler import (
    not_found_handler,
    conflict_handler,
    general_exception_handler
)

# Crear la aplicación FastAPI
app = FastAPI()

# Inicializar la base de datos
init_db()

# Configurar CORS para permitir peticiones desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Registrar routers de controladores
app.include_router(controllerStock.router, prefix="/apiV1", tags=[""])
app.include_router(controllerStats.router, prefix="/apiV1", tags=[""])

# Registrar handlers
app.add_exception_handler(NotFoundError, not_found_handler)
app.add_exception_handler(ConflictError, conflict_handler)
app.add_exception_handler(Exception, general_exception_handler)

"""
Para ejecutar la aplicación, puedes utilizar el siguiente comando:
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

python -m venv venv
source venv/Scripts/activate

"""