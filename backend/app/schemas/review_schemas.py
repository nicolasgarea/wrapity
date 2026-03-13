from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReviewCreate(BaseModel):
    album_id: str
    rating: int
    content: str


class ReviewResponse(BaseModel):
    id: int
    user_id: int
    album_id: str
    rating: int
    content: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReviewUpdate(BaseModel):
    rating: int | None = None
    content: str | None = None
