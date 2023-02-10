from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomDB(MeetingRoomBase):
    id: int

    class Config:
        orm_mode = True


class MeetingRoomUpdate(MeetingRoomDB):

    @validator('name')
    def name_is_not_none(cls, value):
        if value is None:
            raise ValueError('name is None')
        return value
