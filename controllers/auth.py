from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request

from service.auth import AuthManager

auth_router = APIRouter()


@auth_router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await AuthManager.authenticate(form_data)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = AuthManager.create_access_token(data={"id": str(user.id), "email": user.email})
    return {"access_token": access_token, "token_type":"bearer"}

@auth_router.get("/logout")
async def logout(request: Request):
    await AuthManager.logout(request)
    return {"message": "Logged out"}