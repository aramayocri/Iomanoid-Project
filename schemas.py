# Python
from typing import Optional, List
from datetime import datetime
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field, EmailStr, HttpUrl

# Local
from fastapi import UploadFile, File

# Project
class Blockchain(Enum):
    polygon = "Polygon"
    ethereum = "Ethereum"
    solana = "Solana"
    otro = "Otro"

class Marketplace(Enum):
    opensea = "OpenSea"
    rarible = "Rarible"
    otro = "Otro"
    in_process = "En proceso"

class Tags(Enum):
    art = "Art"
    collectible = "Collectible"
    dao = "DAO"
    game = "Game"
    metaverse = "Metaverse"

class Project(BaseModel):
    #project_id: Optional[int]
    project_name: str = Field(..., min_length=1, max_length=50, example="Iomis of Metaverse")
    
    description: str = Field(..., max_length=500, min_length=50)
    owner_id: Optional[int] = Field(default=None)

    blockchain: Blockchain = Field(..., example="Polygon")
    marketplace: Marketplace = Field(..., example="OpenSea")
    marketplace_url: Optional[HttpUrl] = Field(default=None ,example="https://www.opensea.com/collection/iomanoid-genesis")
    collection_size: int = Field(..., gt=0, lt=22223, example=1119)

    release_date: Optional[datetime] = Field(default=None) # NFT drop
    
    instagram: Optional[HttpUrl] = Field(default=None ,example="https://instagram.com/iomanoid_nfts")
    twitter: Optional[HttpUrl] = Field(default=None ,example="https://twitter.com/iomanoid_nfts")
    discord: Optional[HttpUrl] = Field(default=None ,example="https://discord.com/")
    website: Optional[HttpUrl] = Field(default=None ,example="https://iomanoids.com")
    

    tags: Optional[Tags] = Field(default=None, example="Collectible")

    class Config:
        orm_mode = True

class ProjectUpdate(BaseModel):
    project_name: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., max_length=500, min_length=50)

# User
class UserBase(BaseModel):
    user_name: str = Field(
        ...,
        min_length=5,
        max_length=45
    )
    email: EmailStr = Field(...)

class UserRegister(UserBase):
    password: str = Field(...)
    class Config:
        orm_mode = True

class User(UserBase):
    projects: List[Project] = []

    class Config:
        orm_mode = True

class Reply(BaseModel):
    message: str

class Subscriber(BaseModel):
    email: EmailStr = Field(...)
    
    class Config:
        orm_mode = True

# ValidationCode
class ValidationCode(BaseModel):
    code: str = Field(...)
    enabled: bool = Field(default=False)
    class Config:
        orm_mode = True

# PremiumCode
class PremiumCode(BaseModel):
    code: str = Field(...)
    enabled: bool = Field(default=False)
    class Config:
        orm_mode = True
