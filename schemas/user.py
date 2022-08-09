#Python
from typing import Optional, List
from datetime import datetime

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# Local
#from project import Project as SchemaProject


class UserBase(BaseModel):
    user_name: str = Field(
        ...,
        min_length=5,
        max_length=45
    )
    email: EmailStr = Field(...)

class User(UserBase):
    user_id: int
    #is_active: bool = Field(..., default=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)  
    
    #projects: List[SchemaProject] = []

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    pass 

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )
