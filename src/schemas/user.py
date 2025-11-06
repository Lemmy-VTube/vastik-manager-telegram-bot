from datetime import datetime

from pydantic import BaseModel, Field

from src.schemas.roles import UserRole


class UserBase(BaseModel):
    tg_id: int = Field(..., ge=1, description="Telegram ID of the user")
    role: UserRole = Field(default=UserRole.user, description="User role")
    is_new: bool = Field(default=True, description="Indicates whether the user is new")
    accepted_privacy_policy: bool = Field(
        default=False,
        description="Has the user accepted the privacy policy"
    )
    username: str | None = Field(
        None,
        min_length=5,
        max_length=32,
        description="Telegram username of the user (without @, 5–32 chars)"
    )
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=64,
        description="First name of the user in Telegram (1–64 chars)"
    )
    last_name: str | None = Field(
        None,
        min_length=1,
        max_length=64,
        description="Last name of the user in Telegram (1–64 chars)"
    )
    photo_url: str | None = Field(
        None,
        min_length=1,
        max_length=512,
        description="URL of the user's Telegram profile photo (1–512 chars)"
    )


class UserCreate(UserBase):
    ...


class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }