from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import Booking
from app.schemas import BookingCreate, BookingResponse

# Автоматическое создание таблиц в PostgreSQL при запуске
Base.metadata.create_all(bind=engine)

app = FastAPI(title="The Grand Aqtobe API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/bookings", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(booking_data: BookingCreate, db: Session = Depends(get_db)):
    new_booking = Booking(**booking_data.model_dump())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@app.get("/api/v1/bookings", response_model=list[BookingResponse])
def get_all_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()