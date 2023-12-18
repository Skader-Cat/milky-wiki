from fastapi import APIRouter

projects_router = APIRouter()


@projects_router.get("/get_by_name")
async def get_projects():
    pass


@projects_router.post("/create")
async def create_project():
    pass


@projects_router.delete("/delete")
async def delete_project():
    pass


@projects_router.put("/update")
async def update_project():
    pass


@projects_router.get("/list")
async def read_projects():
    pass


@projects_router.get("/get_by_id")
async def read_project():
    pass


@projects_router.get("/get_users")
async def get_project_users():
    pass