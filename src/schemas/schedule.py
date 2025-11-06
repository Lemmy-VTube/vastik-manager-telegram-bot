from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ScheduleBase(BaseModel):
    photo_id: Optional[str] = Field(
        None,
        min_length=1,
        max_length=254,
        description="ID of the photo to be sent (1–254 chars)"
    )
    message_streamer_text: Optional[str] = Field(
        None,
        min_length=1,
        max_length=2000,
        description="Text of the message to be sent by the streamer (1–2000 chars)"
    )


class ScheduleRead(ScheduleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }