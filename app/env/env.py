import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pathlib import Path

# Ruta del directorio actual - directorio donde se encuentra el archivo 'env.py'
dir_proyect = os.path.dirname(os.path.abspath(__file__))

# Ruta de los directorios principales
dir_assets= os.path.join(dir_proyect, '..', 'assets')
dir_controller= os.path.join(dir_proyect, '..', 'controller')
dir_database = os.path.join(dir_proyect, '..', 'database')
dir_model = os.path.join(dir_proyect, '..', 'model')
dir_schemas = os.path.join(dir_proyect, '..', 'schemas')
dir_service = os.path.join(dir_proyect, '..', 'service')

# Ruta hasta la raíz del proyecto para cargar el archivo .env
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

# Configuracion de el usuario y clave para aplicaciones del correo
user_email = os.getenv("USER_EMAIL")
password_email = os.getenv("PASSWORD_EMAIL")

# Datos de conexión
DB_TYPE = "postgresql+psycopg2"
USER = os.getenv("USER")
PASSWORD = quote_plus(os.getenv("PASSWORD"))
HOST = "aws-1-us-east-2.pooler.supabase.com"
PORT = os.getenv("PORT")
DB_NAME = "postgres"

database_url = f"{DB_TYPE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?sslmode=require"