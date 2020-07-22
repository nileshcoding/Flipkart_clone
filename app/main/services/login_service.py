from app.main.settings import *
import jwt

def encode_jwt(payload):
    return jwt.encode(payload,SECRET_KEY)


def decode_auth_token(payload):
    return jwt.decode(payload, SECRET_KEY)
