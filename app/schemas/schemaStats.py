from pydantic import BaseModel
from typing import Optional 

# Esquema para las métricas
class schemaStats(BaseModel):
    id: Optional[int] = None
    metric: int

    # Configuración para permitir la creación de objetos a partir de atributos
    class Config:
        from_attributes = True  

# Actualización de métricas
class schemaStatsUpdate(BaseModel):
    metric: int

    # Configuración para permitir la creación de objetos a partir de atributos
    class Config:
        from_attributes = True  