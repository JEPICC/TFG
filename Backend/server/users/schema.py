from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    id: PyObjectId = Field(alias='_id', default=None)
    username: str
    full_name: str | None = None
    active: bool | None = None

class UserSign(BaseModel):
    username: str
    password: str
    full_name: str | None = None


class UserInDB(User):
    hashed_password: str