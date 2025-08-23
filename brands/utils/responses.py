from rest_framework.response import Response

def success_response(data=None, msg="Operación exitosa", status_code=200):
    return Response({
        "success": True,
        "msg": msg,
        "data": data,
        "errors": None
    }, status=status_code)

def error_response(errors=None, msg="Ocurrió un error", status_code=400):
    return Response({
        "success": False,
        "msg": msg,
        "data": None,
        "errors": errors
    }, status=status_code)
