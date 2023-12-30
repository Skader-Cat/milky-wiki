from sqlalchemy import select

from models.tables import Category
from service.base import Manager


class CategoryManager(Manager):
    db = None

    @classmethod
    async def get_category_list(cls, page, size):
        return await cls.get_list(Category, page, size)

    @classmethod
    async def get_category_by_id(cls, category_id) -> Category:
        return await cls.get_by_id(Category, category_id)

    @classmethod
    async def create_category(cls, category: Category):
        await cls.create(Category, category.model_dump())

    @classmethod
    async def update_category(cls, category_id, category_info):
        await cls.update(Category, category_id, category_info)

    @classmethod
    async def delete_category(cls, category_id):
        await cls.delete(Category, category_id)

    @classmethod
    async def get_category_by_title(cls, title):
        query = select(Category).filter(Category.title == title)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()



