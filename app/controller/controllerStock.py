from fastapi import APIRouter, Depends
from typing import Dict
from sqlalchemy.orm import Session

from schemas.schemaStock import schemaStock
from database.database import conection_db
from utils.success import response
from service.serviceStock import (
    post_stock_service,
    get_stock_by_id,
    get_all_stocks,
    update_stock_service,
    delete_stock_service,
)

router = APIRouter(prefix="/Stock", tags=["Stock"])

# Crear stock
@router.post("/post_stock", summary="Crear Stock")
def post_stock_controller(
    stock: schemaStock,
    db: Session = Depends(conection_db),
) -> Dict:
    nuevo = post_stock_service(db, stock)
    return response(201, schemaStock.model_validate(nuevo))

# Obtener por ID
@router.get("/{stock_id}", summary="Obtener Stock por ID")
def get_stock_by_id_controller(
    stock_id: int,
    db: Session = Depends(conection_db),
) -> Dict:
    stock = get_stock_by_id(db, stock_id)
    return response(200, schemaStock.model_validate(stock))

# Obtener todos
@router.get("/", summary="Obtener todos los Stock")
def get_all_stocks_controller(
    db: Session = Depends(conection_db),
) -> Dict:
    stocks = get_all_stocks(db)
    return response(
        200,
        [schemaStock.model_validate(s) for s in stocks]
    )

# Actualizar
@router.put("/{stock_id}", summary="Actualizar Stock")
def update_stock_controller(
    stock_id: int,
    stock: schemaStock,
    db: Session = Depends(conection_db),
) -> Dict:
    actualizado = update_stock_service(db, stock_id, stock)
    return response(200, schemaStock.model_validate(actualizado))

# Eliminar
@router.delete("/{stock_id}", summary="Eliminar Stock")
def delete_stock_controller(
    stock_id: int,
    db: Session = Depends(conection_db),
) -> Dict:
    delete_stock_service(db, stock_id)
    return response(200, {"message": "Stock eliminado"})