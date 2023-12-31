from fastapi import FastAPI, APIRouter, Depends
from uuid import UUID

from models.schemas.glossary import CreateCategory
from service.category import CategoryManager

category_router = APIRouter()

@category_router.post("/create")
async def create_category(category: CreateCategory):
    await CategoryManager.create_category(category)
    return {"message": "Category created"}

@category_router.get("/get_list")
async def get_category_list(page: int = 1, size: int = 10):
    return await CategoryManager.get_category_list(page, size)

@category_router.get("/get_category_by_id")
async def get_category_by_id(category_id: UUID):
    return await CategoryManager.get_category_by_id(category_id)

@category_router.put("/update")
async def update_category(category_id: UUID, category_info: CreateCategory):
    await CategoryManager.update_category(category_id, category_info)
    return {"message": "Category updated"}

@category_router.delete("/delete")
async def delete_category(category_id: UUID):
    await CategoryManager.delete_category(category_id)
    return {"message": "Category deleted"}

@category_router.get("/get_statistics")
async def get_category_statistics():
    return await CategoryManager.get_category_statistics()


@category_router.get("/get_author_statistics")
async def get_author_statistics():
    return await CategoryManager.get_author_statistics()