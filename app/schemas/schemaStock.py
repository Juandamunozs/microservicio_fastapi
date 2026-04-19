from pydantic import BaseModel
from typing import Optional 

# Esquema para el stock
class schemaStock(BaseModel):
    product_id: Optional[int] = None 
    stock: int

    # Configuración para permitir la creación de objetos a partir de atributos
    class Config:
        from_attributes = True  

# Actualización de stock
class schemaStockUpdate(BaseModel):
    stock: int

    # Configuración para permitir la creación de objetos a partir de atributos
    class Config:
        from_attributes = True  