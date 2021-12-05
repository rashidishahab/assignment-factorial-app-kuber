import jwt
from flask import jsonify, Response, g, request
import json
import config
from flask import g
from app.services.app_exception import InputValidationError, CustomException, AuthenticationException
from app.services.auth_helper import authorize


@authorize
def calculate_factorial_interface():
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException('Request is not valid :{}'.format(e), 406)

    if 'input' not in req_data:
        raise InputValidationError()
    user_input = req_data['input']
    if user_input < 0:
        raise CustomException('The Input should be non-negative number', 406)

    return jsonify({"result": calculate_factorial_func(user_input)})


def calculate_factorial_func(user_input):
    resp = 1

    for i in range(user_input):
        resp = (i+1) * resp

    return resp
