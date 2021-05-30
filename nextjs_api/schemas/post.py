from datetime import datetime
from typing import List

from pydantic import BaseModel


class PostBase(BaseModel):
    """Post Base"""
    title: str
    content: str


class PostCreate(PostBase):
    """Input"""
    pass


class Post(PostBase):
    """Post Output"""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PostList(BaseModel):
    """Posts Output"""
    __root__: List[Post]
