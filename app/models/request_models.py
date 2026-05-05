from pydantic import BaseModel, Field
from typing import Optional


class ContentRequest(BaseModel):
    topic: str = Field(..., min_length=3, description="Topic must be at least 3 characters long")
    platform: str
    tone: str
    duration: Optional[int] = 30
    style: Optional[str] = "default"