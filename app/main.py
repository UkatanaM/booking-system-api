from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Booking, Room, BookingStatus
from app.schemas import BookingCreate, BookingResponse, BookingStatusUpdate

app = FastAPI(title="Luxe Aqtobe API")

# Настройка CORS для взаимодействия с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 1. Изменение статуса бронирования (Admin)
@app.patch("/api/v1/bookings/{booking_id}/status", response_model=BookingResponse)
def update_booking_status(
    booking_id: int, 
    status_data: BookingStatusUpdate, 
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    
    booking.status = status_data.status
    db.commit()
    db.refresh(booking)
    return booking


# 2. Создание бронирования (Client)
@app.post("/api/v1/bookings", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(booking_data: BookingCreate, db: Session = Depends(get_db)):
    # 1. Ищем категорию комнаты
    room = db.query(Room).filter(Room.tier == booking_data.room_tier).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Категория комнаты '{booking_data.room_tier}' не найдена"
        )

    # 2. Проверяем количество уже забронированных комнат этой категории на эти даты
    active_bookings_count = db.query(Booking).filter(
        Booking.room_id == room.id,
        Booking.status.in_([BookingStatus.PENDING, BookingStatus.CONFIRMED]),
        Booking.check_in < booking_data.check_out,
        Booking.check_out > booking_data.check_in
    ).count()

    if active_bookings_count >= room.total_rooms:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="На выбранные даты нет свободных номеров данной категории"
        )

    # 3. Считаем количество ночей и итоговую цену
    nights = (booking_data.check_out - booking_data.check_in).days
    total_price = nights * room.price_per_night

    # 4. Создаем бронь
    booking_dict = booking_data.model_dump(exclude={"room_tier"})
    new_booking = Booking(
        **booking_dict,
        room_id=room.id,
        total_price=total_price,
        status=BookingStatus.PENDING
    )
    
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking