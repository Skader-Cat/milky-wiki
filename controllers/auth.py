from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from service.auth import AuthManager

auth_router = APIRouter()

@auth_router.post("/token")
async def login_for_access_token(request: Request, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await AuthManager.authenticate(form_data)
    if not user:
        return {"error": "Incorrect email or password"}
    access_token = AuthManager.create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await AuthManager.authenticate(form_data)
    if not user:
        return {"error": "Incorrect email or password"}
    access_token = AuthManager.create_access_token(data={"id": str(user.id), "email": user.email})
    return {"access_token": access_token, "token_type":"bearer"}
