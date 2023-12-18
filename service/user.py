import logging

from sqlalchemy import select, insert, delete, update
from models.tables.user import User
from service.base import Manager


class UserManager(Manager):
    db = None

    @classmethod
    async def get_user_by_id(cls, user_id) -> User:
        return await cls.get_by_id(User, user_id)

    @classmethod
    async def get_user_list(cls, page, size):
        return await cls.get_list(User, page, size)

    @classmethod
    async def update_user(cls, user_id, user_info):
        await cls.update(User, user_id, user_info)

    @classmethod
    async def delete_user(cls, user_id):
        await cls.delete(User, user_id)

    @classmethod
    async def create_user(cls, user):
        user_data = user.model_dump()
        user_data["role"] = "user"
        await cls.create(User, user_data)

    @classmethod
    async def get_user_by_username(cls, username) -> User:
        query = select(User).filter(User.username == username)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_user_by_email(cls, email) -> User:
        query = select(User).filter(User.email == email)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_total_users(cls):
        query = select(User)
        result = await cls._execute_query_and_close(query)
        return len(result.scalars().all())
