HTTP_RESPONSES = {
    # Informativos
    100: {"status": "info", "message": "Continuar"},
    101: {"status": "info", "message": "Cambiando protocolos"},
    102: {"status": "info", "message": "Procesando"},

    # 2xx Éxito
    200: {"status": "success", "message": "OK"},
    201: {"status": "success", "message": "Recurso creado"},
    202: {"status": "success", "message": "Aceptado"},
    203: {"status": "success", "message": "Información no autorizada"},
    204: {"status": "success", "message": "Sin contenido"},
    205: {"status": "success", "message": "Restablecer contenido"},
    206: {"status": "success", "message": "Contenido parcial"},
    207: {"status": "success", "message": "Multi-estado"},
    208: {"status": "success", "message": "Ya reportado"},
    226: {"status": "success", "message": "IM usado"},

    # 3xx Redirecciones
    300: {"status": "redirect", "message": "Múltiples opciones"},
    301: {"status": "redirect", "message": "Movido permanentemente"},
    302: {"status": "redirect", "message": "Encontrado"},
    303: {"status": "redirect", "message": "Ver otro"},
    304: {"status": "redirect", "message": "No modificado"},
    305: {"status": "redirect", "message": "Usar proxy"},
    307: {"status": "redirect", "message": "Redirección temporal"},
    308: {"status": "redirect", "message": "Redirección permanente"},

    # 4xx Errores del cliente
    400: {"status": "error", "message": "Solicitud incorrecta"},
    401: {"status": "error", "message": "No autorizado"},
    402: {"status": "error", "message": "Pago requerido"},
    403: {"status": "error", "message": "Prohibido"},
    404: {"status": "error", "message": "No encontrado"},
    405: {"status": "error", "message": "Método no permitido"},
    406: {"status": "error", "message": "No aceptable"},
    407: {"status": "error", "message": "Autenticación de proxy requerida"},
    408: {"status": "error", "message": "Tiempo de espera agotado"},
    409: {"status": "error", "message": "Conflicto"},
    410: {"status": "error", "message": "Recurso eliminado"},
    411: {"status": "error", "message": "Longitud requerida"},
    412: {"status": "error", "message": "Precondición fallida"},
    413: {"status": "error", "message": "Carga demasiado grande"},
    414: {"status": "error", "message": "URI demasiado larga"},
    415: {"status": "error", "message": "Tipo de medio no soportado"},
    416: {"status": "error", "message": "Rango no válido"},
    417: {"status": "error", "message": "Expectativa fallida"},
    418: {"status": "error", "message": "Soy una tetera"},
    421: {"status": "error", "message": "Solicitud mal dirigida"},
    422: {"status": "error", "message": "Entidad no procesable"},
    423: {"status": "error", "message": "Recurso bloqueado"},
    424: {"status": "error", "message": "Dependencia fallida"},
    425: {"status": "error", "message": "Demasiado temprano"},
    426: {"status": "error", "message": "Se requiere actualización"},
    428: {"status": "error", "message": "Precondición requerida"},
    429: {"status": "error", "message": "Demasiadas solicitudes"},
    431: {"status": "error", "message": "Encabezados demasiado grandes"},
    451: {"status": "error", "message": "No disponible por razones legales"},

    # 5xx Errores del servidor
    500: {"status": "error", "message": "Error interno del servidor"},
    501: {"status": "error", "message": "No implementado"},
    502: {"status": "error", "message": "Puerta de enlace incorrecta"},
    503: {"status": "error", "message": "Servicio no disponible"},
    504: {"status": "error", "message": "Tiempo de espera de la puerta de enlace"},
    505: {"status": "error", "message": "Versión HTTP no soportada"},
    506: {"status": "error", "message": "La variante también negocia"},
    507: {"status": "error", "message": "Almacenamiento insuficiente"},
    508: {"status": "error", "message": "Bucle detectado"},
    510: {"status": "error", "message": "No extendido"},
    511: {"status": "error", "message": "Autenticación de red requerida"}
}

def response(code: int, data=None):

    base = HTTP_RESPONSES.get(code, {
        "status": "error",
        "message": "Código no definido"
    })

    return {
        "code": code,
        "status": base["status"],
        "message": base["message"],
        "data": data
    }