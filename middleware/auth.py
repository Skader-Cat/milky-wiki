from fastapi import Depends, exceptions
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



