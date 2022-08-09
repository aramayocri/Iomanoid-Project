# Python
from datetime import datetime
from email.policy import default
from uuid import UUID


#Pydantic
from pydantic import BaseModel, Field

class ValidationCode(BaseModel):
    code: UUID = Field(...)
    enabled: bool = Field(default=False)
