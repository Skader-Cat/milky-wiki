from sqlalchemy import select, func
from sqlalchemy.sql.functions import count

from models.tables import Category
from service import UserManager
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
        query = select(Category).filter(Category.name == title)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_categories_by_names(cls, names):
        query = select(Category).filter(Category.name.in_(names))
        result = await cls._execute_query_and_close(query)
        return result.scalars().all()

    @classmethod
    async def get_category_statistics(cls):
        query = (
            select(
                Category,
                func.count(TerminologyCategory.category_id).label("terminology_count")
            )
            .select_from(
                Category.__table__.join(
                    TerminologyCategory.__table__
                )
            )
            .group_by(Category.id)
        )
        result_data = []
        result = await cls._execute_query_and_close(query)
        for row in result:
            category_data, terminology_count = row
            result_data.append({
                "category": category_data,
                "terminology_count": terminology_count
            })

        return result_data

    @classmethod
    async def get_author_statistics(cls):
        query = (
            select(
                Terminology.author,
                func.count(Terminology.id).label("terminology_count")
            )
            .select_from(
                Terminology.__table__
            )
            .group_by(Terminology.author)
        )
        result_data = []
        result = await cls._execute_query_and_close(query)
        for row in result:
            author_id, terminology_count = row
            result_data.append({
                "author_name": (await UserManager.get_user_by_id(author_id)).email,
                "terminology_count": terminology_count
            })

        return result_data

