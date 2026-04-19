from fastapi import APIRouter, Depends
from typing import Dict
from sqlalchemy.orm import Session

from schemas.schemaStats import schemaStats
from database.database import conection_db
from utils.success import response
from service.serviceStats import (
    post_stats_service,
    get_stats_by_id,
    get_all_stats,
    update_stats_service,
    delete_stats_service,
)

router = APIRouter(prefix="/Stats", tags=["Stats"])

# Crear stats
@router.post("/post_stats", summary="Crear Stats")
def post_stats_controller(
    stats: schemaStats,
    db: Session = Depends(conection_db),
) -> Dict:
    nuevo = post_stats_service(db, stats)
    return response(201, schemaStats.model_validate(nuevo))

# Obtener por ID
@router.get("/{stats_id}", summary="Obtener Stats por ID")
def get_stats_by_id_controller(
    stats_id: int,
    db: Session = Depends(conection_db),
) -> Dict:
    stats = get_stats_by_id(db, stats_id)
    return response(200, schemaStats.model_validate(stats))

# Obtener todos
@router.get("/", summary="Obtener todos los Stats")
def get_all_stats_controller(
    db: Session = Depends(conection_db),
) -> Dict:
    stats = get_all_stats(db)
    return response(
        200,
        [schemaStats.model_validate(s) for s in stats]
    )

# Actualizar
@router.put("/{stats_id}", summary="Actualizar Stats")
def update_stats_controller(
    stats_id: int,
    stats: schemaStats,
    db: Session = Depends(conection_db),
) -> Dict:
    actualizado = update_stats_service(db, stats_id, stats)
    return response(200, schemaStats.model_validate(actualizado))

# Eliminar
@router.delete("/{stats_id}", summary="Eliminar Stats")
def delete_stats_controller(
    stats_id: int,
    db: Session = Depends(conection_db),
) -> Dict:
    delete_stats_service(db, stats_id)
    return response(200, {"message": "Stats eliminado"})