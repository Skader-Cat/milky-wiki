from fastapi import APIRouter, Depends

from models import schemas
from service import UserManager
from service.auth import AuthManager

users_router = APIRouter()


@users_router.post("/create")
async def create_user(user: schemas.UserCreate):
    user.password = AuthManager.get_password_hash(user.password)
    await UserManager.create_user(user)
    return {"status": "User created"}

@users_router.delete("/delete")
async def delete_user(user_id: str):
    await UserManager.delete_user(user_id)

@users_router.get("/me", response_model=schemas.UserResponse)
async def read_users_me(current_user: schemas.UserResponse = Depends(AuthManager.get_current_user)):
    return current_user

@users_router.get("/user/{user_id}", response_model=schemas.UserResponse)
async def read_user(user_id: str):
    return await UserManager.get_user_by_id(user_id)

@users_router.put("/update", response_model=schemas.UserUpdate)
async def update_user(user: schemas.UserUpdate):
    await UserManager.update_user(user.id, user)

@users_router.get("/list", response_model=schemas.UserListResponse)
async def read_users(page: int = 1, size: int = 10):
    users = await UserManager.get_user_list(page, size)
    total_users = await UserManager.get_total_users()
    return {"users": users, "total": total_users, "page": page, "size": size}


@users_router.get("/get_by_email", response_model=schemas.UserResponse)
async def get_user_by_email(email: str):
    return await UserManager.get_user_by_email(email)

@users_router.get("/get_role", response_model=schemas.UserResponse)
async def get_user_role(user_id: str):
    return await UserManager.get_user_role(user_id)

@users_router.get("/get_projects")
async def get_user_projects(user_id: str):
    return await UserManager.get_user_projects(user_id)