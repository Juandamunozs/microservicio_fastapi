from sqlalchemy.orm import Session
from model.modelStock import Stock
from schemas.schemaStock import schemaStock

# Excepciones personalizadas
class NotFoundError(Exception):
    pass

class ConflictError(Exception):
    pass

# Servicio para crear un nuevo stock
def post_stock_service(db: Session, stock: schemaStock):

    # Buscar si ya existe un stock con ese ID
    existe_stock = db.query(Stock).filter(Stock.product_id == stock.product_id).first()
    
    if existe_stock:
        raise ConflictError("El stock ya existe")

    # Convertir el schema (Pydantic) a diccionario
    stock_data = stock.model_dump()

    # Crear instancia del modelo SQLAlchemy
    nuevo_stock = Stock(**stock_data)

    # Guardar en la base de datos
    db.add(nuevo_stock)
    db.commit()
    db.refresh(nuevo_stock)  # Actualiza el objeto con datos de la BD

    return nuevo_stock

# Servicio para obtener un stock por ID
def get_stock_by_id(db: Session, stock_id: int):

    stock = db.query(Stock).filter(Stock.product_id == stock_id).first()
    
    if not stock:
        raise NotFoundError("Stock no encontrado")
    
    return stock

# Servicio para obtener todos los stocks
def get_all_stocks(db: Session):
    return db.query(Stock).all()

# Servicio para actualizar un stock
def update_stock_service(db: Session, stock_id: int, stock: schemaStock):

    # Buscar el registro en la base de datos
    stock_db = db.query(Stock).filter(Stock.product_id == stock_id).first()
    
    if not stock_db:
        raise NotFoundError("Stock no encontrado")

    # Convertir schema a diccionario
    stock_data = stock.model_dump(exclude_unset=True)

    # Actualizar atributos dinámicamente
    for key, value in stock_data.items():
        setattr(stock_db, key, value)

    # Guardar cambios
    db.commit()
    db.refresh(stock_db)

    return stock_db

# Servicio para eliminar un stock
def delete_stock_service(db: Session, stock_id: int):
    stock_db = db.query(Stock).filter(Stock.product_id == stock_id).first()
    
    if not stock_db:
        raise NotFoundError("Stock no encontrado")

    db.delete(stock_db)
    db.commit()

    return True