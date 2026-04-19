from fastapi import Request
from fastapi.responses import JSONResponse

from utils.success import response
from service.serviceStock import NotFoundError, ConflictError


# 404 - No encontrado
async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content=response(404)
    )


# 409 - Conflicto
async def conflict_handler(request: Request, exc: ConflictError):
    return JSONResponse(
        status_code=409,
        content=response(409)
    )


# 500 - Error general
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=response(500)
    )