from pydantic import BaseModel
from typing import Optional

class Pet(BaseModel):
    user_id: int
    name: str
    species: str
    age: int
    gender: str
    description: str
    image_url: Optional[str] = None
    status: Optional[str] = "available"