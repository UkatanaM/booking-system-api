from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base


class BookingStatus(str, PyEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    tier = Column(String, unique=True, nullable=False)  # например: deluxe, executive, panorama, presidential
    name = Column(String, nullable=False)
    price_per_night = Column(Integer, nullable=False)
    total_rooms = Column(Integer, default=5)  # Сколько всего комнат этой категории в отеле

    bookings = relationship("Booking", back_populates="room")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    guests = Column(Integer, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    special_requests = Column(String, nullable=True)

    status = Column(Enum(BookingStatus), default=BookingStatus.PENDING, nullable=False)
    total_price = Column(Integer, nullable=False, default=0)

    room = relationship("Room", back_populates="bookings")