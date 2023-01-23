import datetime

import jwt
from rest_framework_simplejwt import exceptions


def create_access_token(id):
    return jwt.encode({
        'user_id' : id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30), #expiry time
        'iat' : datetime.datetime.utcnow(),  #current time
    },'access_secret',algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token,'access_secret',algorithms='HS256')
        return payload('user_id')
    except:
        raise exceptions.AuthenticationFailed('unauthorized')

def create_refresh_token(id):
    return jwt.encode({
        'user_id' : id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=7), #expiry time
        'iat' : datetime.datetime.utcnow(),  #current time
    },'refresh_secret',algorithm='HS256')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token,'refresh_secret',algorithms='HS256')
        return payload('user_id')
    except:
        raise exceptions.AuthenticationFailed('unauthorized')