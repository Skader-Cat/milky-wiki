from fastapi import APIRouter, Depends

from models.schemas.project import ProjectCreate
from service.auth import AuthManager
from service.project import ProjectManager

projects_router = APIRouter()


@projects_router.post("/create")
async def create_project(project: ProjectCreate,
                         current_user: AuthManager = Depends(AuthManager.get_current_user)):
    await ProjectManager.create_project(project, current_user)

@projects_router.get("/list")
async def get_project_list(page: int = 1, size: int = 10):
    projects = await ProjectManager.get_project_list(page, size)
    total_projects = await ProjectManager.get_total_projects()
    return {"projects": projects, "total": total_projects, "page": page, "size": size}

@projects_router.get("/list_by_user")
async def get_project_list_by_user(user_id: str, page: int = 1, size: int = 10):
    projects = await ProjectManager.get_project_list_by_user(user_id, page, size)
    total_projects = await ProjectManager.get_total_projects()
    return {"projects": projects, "total": total_projects, "page": page, "size": size}

@projects_router.get("/get_by_name")
async def get_project_by_name(name: str):
    return await ProjectManager.get_project_by_name(name)

@projects_router.get("/get_users")
async def get_project_users(project_id: str):
    return await ProjectManager.get_project_users(project_id)

@projects_router.post("/add_user")
async def add_user_to_project(project_id: str, user_id: str):
    return await ProjectManager.add_user_to_project(project_id, user_id)

@projects_router.delete("/remove_user")
async def remove_user_from_project(project_id: str, user_id: str):
    return await ProjectManager.remove_user_from_project(project_id, user_id)

@projects_router.delete("/delete")
async def delete_project(project_id: str):
    await ProjectManager.delete_project(project_id)
    return {"status": "Project deleted"}

@projects_router.get("/get_by_id")
async def get_project_by_id(project_id: str):
    return await ProjectManager.get_project_by_id(project_id)

@projects_router.put("/update")
async def update_project(project_id: str, project_info: dict):
    await ProjectManager.update_project(project_id, project_info)
    return {"status": "Project updated"}

@projects_router.get("/get_total")
async def get_total_projects():
    return await ProjectManager.get_total_projects()



