import os

# Ruta del directorio actual - directorio donde se encuentra el archivo 'env.py'
dir_proyect = os.path.dirname(os.path.abspath(__file__))

# Ruta de los directorios principales
dir_assets= os.path.join(dir_proyect, '..', 'assets')
dir_controller= os.path.join(dir_proyect, '..', 'controller')
dir_database = os.path.join(dir_proyect, '..', 'database')
dir_model = os.path.join(dir_proyect, '..', 'model')
dir_schemas = os.path.join(dir_proyect, '..', 'schemas')
dir_service = os.path.join(dir_proyect, '..', 'service')

# Configuracion de el usuario y clave para aplicaciones del correo
user_email = "lifesnapco@gmail.com"
password_email = "bhcf jhfk jvkw ibro"

# Ruta de la base de datos
database_url = "sqlite:///./stock.db"