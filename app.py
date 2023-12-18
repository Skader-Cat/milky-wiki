from fastapi import FastAPI
import controllers.auth
from lifespan import main_app_lifespan

import settings

app = FastAPI(
    lifespan=main_app_lifespan,
    **settings.AppSettings.get_properties()
)

app.include_router(controllers.auth_router, prefix="/auth", tags=["auth"])
app.include_router(controllers.users_router, prefix="/users", tags=["users"])
app.include_router(controllers.projects_router, prefix="/projects", tags=["projects"])