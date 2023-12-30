from models.schemas import AddTerminology
from models.tables import Glossary
from service.base import Manager


class GlossaryManager(Manager):
    db = None

    @classmethod
    async def add_terminology(cls, terminology: AddTerminology):
        await cls.create(Glossary, terminology.model_dump())
