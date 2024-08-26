from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserInDB(BaseModel):
    id: int
    username: str
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str
