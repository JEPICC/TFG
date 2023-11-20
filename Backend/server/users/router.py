from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Annotated
from server.users.schema import User, Token, UserSign
from server.users.models import get_user, create_new_user
from server.users.util import (
    authenticate_user, 
    get_current_active_user, 
    create_access_token,
    get_password_hash)

users = APIRouter(prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
    )
@users.post('/signup', summary="Create new user")
async def create_user(data: UserSign):
    # querying database to check if user already exist
    user = await get_user(data.username)
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'username': data.username,
        'password': get_password_hash(data.password),
        'full_name:': data.full_name,
        'active:': False
    }
    new_user = await create_new_user(user)  # saving user to database
    return new_user

@users.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=10)
    access_token = create_access_token(
        data={"sub": user['username']}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@users.get("/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@users.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]