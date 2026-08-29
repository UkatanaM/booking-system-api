from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, model_validator


class BookingBase(BaseModel):
    room_tier: str
    check_in: date
    check_out: date
    guests: int = Field(..., ge=1, description="Минимум 1 гость")
    full_name: str
    email: EmailStr
    phone: str
    special_requests: Optional[str] = None


class BookingCreate(BookingBase):

    @model_validator(mode="after")
    def validate_dates(self):
        if self.check_in < date.today():
            raise ValueError("Дата заезда не может быть в прошлом")
        if self.check_out <= self.check_in:
            raise ValueError("Дата выезда должна быть строго позже даты заезда")
        return self


class BookingResponse(BookingBase):
    id: int

    class Config:
        from_attributes = True

class BookingStatusUpdate(BaseModel):
    status: BookingStatus

class RoomResponse(BaseModel):
    id: int
    tier: str
    name: str
    price_per_night: int
    total_rooms: int

    class Config:
        from_attributes = True