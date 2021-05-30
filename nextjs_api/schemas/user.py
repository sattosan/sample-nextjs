from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    """User Base"""
    name: str


class UserCreate(UserBase):
    """Input"""
    password: str


class User(UserBase):
    """User Output"""
    id: int

    class Config:
        orm_mode = True


class UserList(BaseModel):
    """Users Output"""
    __root__: List[User]
