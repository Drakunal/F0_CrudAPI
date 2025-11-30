from pydantic import BaseModel, Field
from typing import Optional

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "My item",
                "description": "A short description"
            }
        }

class ItemRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
        
class ItemUpdate(BaseModel):
    name: str
    description: Optional[str] = None

