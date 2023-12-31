import datetime

from sqlalchemy import select, Select, func
from sqlalchemy.orm import joinedload, Query, join

from models.schemas import AddTerminology
from models.tables import Glossary, Terminology, TerminologyCategory, Category, User
from service.base import Manager
from service.category import CategoryManager


class GlossaryManager(Manager):
    db = None

    @classmethod
    async def add_terminology(cls, terminology: AddTerminology, user: User):
        categories = await CategoryManager.get_categories_by_names(terminology.categories)
        terminology_data = terminology.model_dump(exclude={"categories"})
        terminology_data["created_at"] = datetime.datetime.now()
        terminology_data["author"] = user.id
        terminology_data["id"] = await cls.create(Terminology, terminology_data)
        print(terminology_data)
        # Ensure terminology_data["id"] is set properly
        if not terminology_data["id"]:
            # Handle the case where ID is not set
            raise ValueError("Failed to retrieve ID for Terminology")

        data = [
            {
                "termin_id": terminology_data["id"],
                "category_id": category.id
            }
            for category in categories
        ]

        if data:
            await cls.create(TerminologyCategory, data)
        else:
            raise ValueError("No categories found for the given names")


    @classmethod
    async def get_terminology_list(cls, page, size):
        query = (
            select(
                Terminology,
                func.array_agg(Category.name).label('categories')
            )
            .select_from(
                Terminology.__table__.join(
                    TerminologyCategory.__table__
                ).join(
                    Category.__table__
                )
            )
            .group_by(Terminology.id)
            .offset((page - 1) * size)
            .limit(size)
        )
        result_data = []
        result = await cls._execute_query_and_close(query)

        for row in result:
            terminology_data, category_data = row
            result_data.append({
                "terminology": terminology_data,
                "categories": category_data
            })

        return result_data

