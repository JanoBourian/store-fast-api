from config.config import env
from connection.database import database
from connection.models import Users
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status
from starlette.requests import Request
from typing import Optional
import jwt
import logging
import datetime


def create_access_token(user):
    try:
        payload = {
            "sub": user["id"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
        }
        return jwt.encode(payload, env("JWT_SECRET"), algorithm="HS256")
    except Exception as e:
        logging.warning(f"Exception {e}")
        raise e


class CustomHTTPBearer(HTTPBearer):
    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        try:
            payload = jwt.decode(
                res.credentials, env("JWT_SECRET"), algorithms=["HS256"]
            )
            user = await database.fetch_one(
                Users.select().where(Users.c.id == payload["sub"])
            )
            request.state.user = user
            return payload
        except jwt.ExpiredSignatureError as e:
            logging.info(f"Exception {e}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Token is expired"
            )
        except jwt.InvalidTokenError as e:
            logging.info(f"Exception {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )


def is_admin(request: Request):
    user = request.state.user
    if not user or user["role"] not in ("admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission for this resource",
        )


oauth2_scheme = CustomHTTPBearer()
