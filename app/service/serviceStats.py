from sqlalchemy.orm import Session
from model.modelStats import Stats
from schemas.schemaStats import schemaStats

# Excepciones personalizadas
class NotFoundError(Exception):
    pass

class ConflictError(Exception):
    pass

# Servicio para crear un nueva stats
def post_stats_service(db: Session, stats: schemaStats):

    # Buscar si ya existe un stats con ese ID
    existe_stats = db.query(Stats).filter(Stats.id  == Stats.id ).first()
    
    if existe_stats:
        raise ConflictError("La métrica ya existe")

    # Convertir el schema (Pydantic) a diccionario
    stats_data = stats.model_dump()

    # Crear instancia del modelo SQLAlchemy
    nuevo_stats = Stats(**stats_data)

    # Guardar en la base de datos
    db.add(nuevo_stats)
    db.commit()
    db.refresh(nuevo_stats)  # Actualiza el objeto con datos de la BD

    return nuevo_stats

# Servicio para obtener un stats por ID
def get_stats_by_id(db: Session, stats_id: int):

    stats = db.query(Stats).filter(Stats.id == stats_id).first()
    
    if not stats:
        raise NotFoundError("Stats no encontrada")
    
    return stats

# Servicio para obtener todos los statss
def get_all_stats(db: Session):
    return db.query(Stats).all()

# Servicio para actualizar un stats
def update_stats_service(db: Session, stats_id: int, stats: schemaStats):

    # Buscar el registro en la base de datos
    stats_db = db.query(Stats).filter(Stats.id  == stats_id).first()
    
    if not stats_db:
        raise NotFoundError("Stats no encontrada")

    # Convertir schema a diccionario
    stats_data = stats.model_dump(exclude_unset=True)

    # Actualizar atributos dinámicamente
    for key, value in stats_data.items():
        setattr(stats_db, key, value)

    # Guardar cambios
    db.commit()
    db.refresh(stats_db)

    return stats_db

# Servicio para eliminar un stats
def delete_stats_service(db: Session, stats_id: int):
    stats_db = db.query(Stats).filter(Stats.id  == stats_id).first()
    
    if not stats_db:
        raise NotFoundError("Stats no encontrada")

    db.delete(stats_db)
    db.commit()

    return True

# Servicio opcional para validación (puedes expandir lógica aquí)
def update_stats_service_validation(db: Session, stats_id: int):
    stats = db.query(Stats).filter(Stats.id  == stats_id).first()
    
    if not stats:
        raise NotFoundError("Stats no encontrada")

    return stats