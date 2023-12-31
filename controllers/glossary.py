from fastapi import APIRouter, Depends

from models.schemas import AddTerminology
from service.auth import AuthManager
from service.glossary import GlossaryManager

glossary_router = APIRouter()


@glossary_router.post("/add_terminology")
async def create_terminology(terminology: AddTerminology,
                             current_user: AuthManager = Depends(AuthManager.get_current_user)):
    await GlossaryManager.add_terminology(terminology, current_user)
    return {"message": "Terminology created"}

@glossary_router.get("/get_terminology_list")
async def get_terminology_list(page: int = 1, size: int = 10):
    return await GlossaryManager.get_terminology_list(page, size)


@glossary_router.get("/save_terminology_report")
async def save_terminology():
    terminology_list = await GlossaryManager.get_terminology_list(1, 100000)

