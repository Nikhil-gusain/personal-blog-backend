import dotsi
from rest_framework.response import Response
def LocalResponse(response='', message='', data={}, code=1):
    obj = {
        'code': code,
        'message': message,
        'data': data,
    }
    model = dotsi.Dict(obj)
    return model

def ServerResponse(response='', message='', data={}, code=1):
    obj = {
        'code': code,
        'message': message,
        'data': data,
    }
    return Response(obj)