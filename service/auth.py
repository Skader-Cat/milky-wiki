import datetime
from uuid import UUID

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext

import credits
from models.tables import User
from service import UserManager


class AuthManager(object):
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def __init__(self):
        pass

    @classmethod
    def verify_password(cls, password, hashed_password):
        return cls.pwd_context.verify(password, hashed_password)

    @classmethod
    def get_password_hash(cls, password):
        return cls.pwd_context.hash(password)

    @classmethod
    async def authenticate(cls, form_data, db):
        user = await UserManager.get_user_by_email(form_data.username, db)
        if not user:
            return False
        print(form_data.password, user.password)
        if not cls.verify_password(form_data.password, user.password):
            return False
        return user

    @classmethod
    async def get_current_user(cls, token: str) -> User:
        payload = jwt.decode(token, credits.AUTH.SECRET_KEY, algorithms=[credits.AUTH.ALGORITHM])
        user_id: UUID =  payload.get("id")
        if user_id is None:
            raise Exception("Invalid token")
        return await UserManager.get_user_by_id(user_id)

    @classmethod
    async def get_admin_user(cls, token: str) -> User:
        payload = jwt.decode(token, credits.AUTH.SECRET_KEY, algorithms=[credits.AUTH.ALGORITHM])
        user_id: UUID =  payload.get("id")
        if user_id is None:
            raise Exception("Invalid token")
        user = await UserManager.get_user_by_id(user_id)
        if user.role != "admin":
            raise HTTPException(status_code=403, detail="Unauthorized user")
        return user

    @classmethod
    def create_access_token(cls, data: dict) -> str:
        to_encode = data.copy()
        expires = datetime.datetime.now() + datetime.timedelta(minutes=credits.AUTH.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expires})
        encoded_jwt = jwt.encode(to_encode, credits.AUTH.SECRET_KEY, algorithm=credits.AUTH.ALGORITHM)
        return encoded_jwt