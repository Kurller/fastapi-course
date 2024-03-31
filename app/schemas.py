from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    post: Post
    votes: int

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    email: EmailStr
    posts: List[Post] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: int
    
