from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator
from app.models import BookingStatus


class BookingBase(BaseModel):
    check_in: date
    check_out: date
    guests: int = Field(..., ge=1, description="Минимум 1 гость")
    full_name: str
    email: EmailStr
    phone: str
    special_requests: Optional[str] = None


class BookingCreate(BookingBase):
    room_tier: str

    @model_validator(mode="after")
    def validate_dates(self):
        if self.check_in < date.today():
            raise ValueError("Дата заезда не может быть в прошлом")
        if self.check_out <= self.check_in:
            raise ValueError("Дата выезда должна быть строго позже даты заезда")
        return self


class BookingResponse(BookingBase):
    id: int
    room_id: int
    status: BookingStatus
    total_price: int

    model_config = ConfigDict(from_attributes=True)


class RoomResponse(BaseModel):
    id: int
    tier: str
    name: str
    price_per_night: int
    total_rooms: int

    model_config = ConfigDict(from_attributes=True)


class BookingStatusUpdate(BaseModel):
    status: BookingStatus