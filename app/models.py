from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    room_tier = Column(String, nullable=False)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    guests = Column(Integer, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    special_requests = Column(String, nullable=True)