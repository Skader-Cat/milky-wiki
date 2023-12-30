from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import controllers.auth
from lifespan import main_app_lifespan

import settings

app = FastAPI(
    lifespan=main_app_lifespan,
    **settings.AppSettings.get_properties()
)

app.add_middleware(CORSMiddleware,
                   allow_origins=settings.CORSSettings.ALLOW_ORIGINS,
                   allow_methods=settings.CORSSettings.ALLOW_METHODS,
                   allow_headers=settings.CORSSettings.ALLOW_HEADERS,
                   allow_credentials=settings.CORSSettings.ALLOW_CREDENTIALS,
                   allow_origin_regex=settings.CORSSettings.ALLOW_ORIGIN_REGEX,
                   expose_headers=settings.CORSSettings.EXPOSE_HEADERS,
                   max_age=settings.CORSSettings.MAX_AGE
                   )

app.include_router(controllers.auth_router, prefix="/auth", tags=["auth"])
app.include_router(controllers.users_router, prefix="/users", tags=["users"])
app.include_router(controllers.projects_router, prefix="/projects", tags=["projects"])
app.include_router(controllers.notes_router, prefix="/notes", tags=["notes"])
app.include_router(controllers.category_router, prefix="/category", tags=["category"])
app.include_router(controllers.glossary_router, prefix="/glossary", tags=["glossary"])