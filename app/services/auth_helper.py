import datetime
import re
from functools import wraps

import jwt
from flask import abort, request, g

import config
from app.services.app_exception import AuthenticationException


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if 'X-API-KEY' not in request.headers or len(request.headers.get('X-API-KEY')) < 2:
            raise AuthenticationException()

        try:
            token = request.headers.get('X-API-KEY', None)
            if token != config.X_API_KEY:
                raise AuthenticationException()
        except Exception:
            raise AuthenticationException()

        return f(*args, **kws)

    return decorated_function
