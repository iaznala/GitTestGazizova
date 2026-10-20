from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

class Event(BaseModel):
    id: Optional[UUID] = None
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomymage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }