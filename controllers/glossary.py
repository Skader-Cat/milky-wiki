from fastapi import APIRouter

from models.schemas import AddTerminology
from service.glossary import GlossaryManager

glossary_router = APIRouter()


@glossary_router.get("add_terminology")
async def create_terminology(terminology: AddTerminology):
    await GlossaryManager.add_terminology(terminology)
    return {"message": "Terminology created"}
