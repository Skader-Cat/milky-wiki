from sqlalchemy import select, insert, update, delete

from db import DatabaseManager, DB_Manager


class Manager:
    @classmethod
    async def _execute_query(cls, query):
        async with await DB_Manager.get_session() as session:
            result = await session.execute(query)
            return result

    @classmethod
    async def _execute_query_and_close(cls, query):
        result = await cls._execute_query(query)
        return result

    @classmethod
    async def get_by_id(cls, model, id):
        query = select(model).filter(model.id == id)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_list(cls, model, page, size):
        query = select(model).offset((page - 1) * size).limit(size)
        result = await cls._execute_query_and_close(query)
        return result.scalars().all()

    @classmethod
    async def create(cls, model, data):
        query = insert(model).values(data)
        await cls._execute_query_and_close(query)

    @classmethod
    async def update(cls, model, id, data):
        query = update(model).where(model.id == id).values(data)
        await cls._execute_query_and_close(query)

    @classmethod
    async def delete(cls, model, id):
        query = delete(model).where(model.id == id)
        await cls._execute_query_and_close(query)


