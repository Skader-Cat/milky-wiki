import datetime
from uuid import UUID

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.sql import roles
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

import credits
import settings
from models import schemas
from models.tables import User
from service import UserManager
from service.base import Manager

class AuthManager(Manager):
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

    def __init__(self):
        pass

    @classmethod
    async def logout(cls, request):
        request.state.user = None


    @classmethod
    def verify_password(cls, password, hashed_password):
        return cls.pwd_context.verify(password, hashed_password)

    @classmethod
    def get_password_hash(cls, password):
        return cls.pwd_context.hash(password)

    @classmethod
    async def authenticate(cls, form_data):
        user = await UserManager.get_user_by_email(form_data.username)
        if not user:
            return False
        print(form_data.password, user.password)
        if not cls.verify_password(form_data.password, user.password):
            return False
        return user

    @classmethod
    async def get_current_user(cls, token: str) -> schemas.UserResponse:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            payload = jwt.decode(token, credits.AUTH.SECRET_KEY, algorithms=[credits.AUTH.ALGORITHM])
            id: str = payload.get("id")
            if id is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = await UserManager.get_user_by_id(id)
        if not user:
            raise credentials_exception

        if user.role not in settings.ALLOWED_ROLES.get_properties():
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )

        return await UserManager.get_user_by_id(user.id)


    @classmethod
    def create_access_token(cls, data: dict) -> str:
        to_encode = data.copy()
        expires = datetime.datetime.now() + datetime.timedelta(minutes=credits.AUTH.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expires})
        encoded_jwt = jwt.encode(to_encode, credits.AUTH.SECRET_KEY, algorithm=credits.AUTH.ALGORITHM)
        return encoded_jwt