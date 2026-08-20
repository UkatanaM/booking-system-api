from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class BookingCreate(BaseModel):
    room_tier: str
    check_in: date
    check_out: date
    guests: int
    full_name: str
    email: EmailStr
    phone: str
    special_requests: Optional[str] = None

class BookingResponse(BookingCreate):
    id: int

    class Config:
        from_attributes = True