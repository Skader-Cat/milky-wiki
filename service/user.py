import logging

from sqlalchemy import select, insert, delete, update
from models.tables.user import User

class UserManager(object):
    db = None

    @classmethod
    async def _execute_query(cls, query):
        async with cls.db as session:
            result = await session.execute(query)
            await session.commit()
            return result

    @classmethod
    async def _execute_query_and_close(cls, query):
        result = await cls._execute_query(query)
        session = cls.db
        await session.close()
        return result

    @classmethod
    async def get_user_by_id(cls, user_id) -> User:
        query = select(User).filter(User.id == user_id)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_user_by_username(cls, username) -> User:
        query = select(User).filter(User.username == username)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_user_list(cls, page, size):
        query = select(User).offset((page - 1) * size).limit(size)
        result = await cls._execute_query_and_close(query)
        return result.scalars().all()

    @classmethod
    async def get_user_by_email(cls, email) -> User:
        query = select(User).filter(User.email == email)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def create_user(cls, user):
        user_data = user.model_dump()
        user_data["role"] = "user"
        query = insert(User).values(user_data)
        await cls._execute_query_and_close(query)

    @classmethod
    async def update_user(cls, user_id, user_info):
        query = update(User).where(User.id == user_id).values(user_info)
        await cls._execute_query_and_close(query)

    @classmethod
    async def delete_user(cls, user_id):
        query = delete(User).where(User.id == user_id)
        await cls._execute_query_and_close(query)

    @classmethod
    async def get_total_users(cls):
        query = select(User)
        result = await cls._execute_query_and_close(query)
        return len(result.scalars().all())
