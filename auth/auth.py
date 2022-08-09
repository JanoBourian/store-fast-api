from config.config import env
import jwt
import logging
import datetime

def create_access_token(user):
    try:
        payload = {"sub": user["id"], "exp": datetime.datetime.now() + datetime.timedelta(minutes=120)}
        return jwt.encode(payload, env("JWT_SECRET"), algorithm="HS256")
    except Exception as e:
        logging.warning(f"Exception {e}")
        raise e
        