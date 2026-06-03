# schemas.py
from pydantic import BaseModel
from typing import Optional

class ResidentCreate(BaseModel):
    resident_name: str
    apartment: str
    block: str
    relatives: Optional[str] = None
    cleaner: Optional[str] = None

class ResidentResponse(BaseModel):
    id: int
    resident_name: str
    apartment: str
    block: str
    relatives: Optional[str]
    cleaner: Optional[str]

    class Config:
        from_attributes = True