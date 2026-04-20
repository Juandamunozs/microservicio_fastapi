from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from env.env import database_url

# Configurar la conexión a la base de datos
engine = create_engine(
    database_url,
    poolclass=NullPool,   # evita conflictos con pgbouncer
    pool_pre_ping=True    # evita conexiones muertas
)

# Crear una sesión local
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Crear la clase base para los modelos
Base = declarative_base()

# Dependency para FastAPI
def conection_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear tablas
def init_db():
    Base.metadata.create_all(bind=engine)