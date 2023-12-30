from sqlalchemy import select

from models import schemas
from models.tables.project import Project_User, Project
from models.tables.user import User
from service.base import Manager


class UserManager(Manager):
    db = None

    @classmethod
    async def get_user_by_id(cls, user_id) -> schemas.UserResponse:
        return await cls.get_by_id(User, user_id)

    @classmethod
    async def search_user(cls, search_query, page, size):
        query = select(User).filter(User.username.like(f"%{search_query}%")).offset((page - 1) * size).limit(size)
        result = await cls._execute_query_and_close(query)
        return result.scalars().all()

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

    @classmethod
    async def get_user_role(cls, user_id):
        query = select(User.role).filter(User.id == user_id)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()[0]

    @classmethod
    async def get_user_projects(cls, user_id):
        projects = select(Project).join(Project_User).filter(Project_User.user_id == user_id)
        result = await cls._execute_query_and_close(projects)
        return result.scalars().all()

    @classmethod
    async def search(cls, search_query, page, size):
        query = select(User).filter(User.username.like(f"%{search_query}%")).offset((page - 1) * size).limit(size)
        result = await cls._execute_query_and_close(query)
        return result.scalars().all()