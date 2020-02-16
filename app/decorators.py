from functools import wraps
from flask import abort, request, jsonify
from flask_login import current_user
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, '1234', algorithm='HS256')

        except:
            return jsonify({'message' : 'Token is invalid'}), 403

        return f(*args, **kwargs)
    return decorated


# def forum_permission(permission):
#     def decorator(f):
#         @wraps(f)
#         def decorated_function(*args, **kwargs):
#             if not current_user.can_forum(permission):

def admin_required(f):
    #wow, this is crazy smart (the first part of the function)
    #is executed and depending on the outcome, the return value is
    #the decorated_function and decorator
    return permission_required(Permission.ADMINISTRATOR)(f)
