from typing import Optional, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
import settings
from models.schemas import UserResponse
from models.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from service import UserManager
from service.auth import AuthManager
from service.project import ProjectManager

projects_router = APIRouter()


@projects_router.post("/create")
async def create_project(project: ProjectCreate,
                         current_user: AuthManager = Depends(AuthManager.get_current_user)):
    if current_user.role == "guest":
        raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        await ProjectManager.create_project(project, current_user)

@projects_router.get("/list")
async def get_project_list(page: int = 1, size: int = 10):
    projects = await ProjectManager.get_project_list(page, size)
    total_projects = await ProjectManager.get_total_projects()
    return {"projects": projects, "total": total_projects, "page": page, "size": size}

@projects_router.get("/get_list_by_user_id", response_model=List[ProjectResponse])
async def get_project_list_by_user(user_id: str, page: int = 1, size: int = 10):
    projects = await ProjectManager.get_project_list_by_user(user_id, page, size)
    return projects

@projects_router.get("/get_by_name")
async def get_project_by_name(name: str):
    return await ProjectManager.get_project_by_title(name)

@projects_router.get("/get_users", response_model=List[UserResponse])
async def get_project_users(project_id: str, current_user: AuthManager = Depends(AuthManager.get_current_user)):
    return (await ProjectManager.get_project_users(project_id))


class HTTPEXception:
    pass


@projects_router.post("/add_user")
async def add_user_to_project(project_id: str, email: str, user_id: Optional[str] = None, current_user: AuthManager = Depends(AuthManager.get_current_user)):
    if not user_id and not email:
        raise HTTPException(status_code=400, detail="No user_id or email provided")

    if not user_id and email:
        user = await UserManager.get_user_by_email(email)
        user_id = user.id

    project_users = await ProjectManager.get_project_users(project_id)
    if any(user.id == user_id for user in project_users):
        raise HTTPException(status_code=400, detail="User is already a member of the project")

    if (
            current_user.role == settings.ALLOWED_ROLES.MANAGER or
            current_user.id == (await ProjectManager.get_project_by_id(project_id)).owner_id
    ):
        return await ProjectManager.add_user_to_project(project_id, user_id)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@projects_router.delete("/remove_user")
async def remove_user_from_project(project_id: str, user_id: str, current_user: AuthManager = Depends(AuthManager.get_current_user)):
    if (
            current_user.role == "moder" or
            current_user.id == (await ProjectManager.get_project_by_id(project_id)).owner_id
    ):
        return await ProjectManager.remove_user_from_project(project_id, user_id)

    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@projects_router.delete("/delete")
async def delete_project(project_id: str):
    await ProjectManager.delete_project(project_id)
    return {"status": "Project deleted"}

@projects_router.get("/get_by_id")
async def get_project_by_id(project_id: UUID):
    return await ProjectManager.get_project_by_id(project_id)

@projects_router.put("/update")
async def update_project(project_id: str, project_info: ProjectUpdate):
    await ProjectManager.update_project(project_id, project_info)
    return {"status": "Project updated"}

@projects_router.get("/get_total")
async def get_total_projects():
    return await ProjectManager.get_total_projects()


