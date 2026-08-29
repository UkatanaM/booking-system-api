from datetime import date, timedelta
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# 1. Проверка получения списка комнат
def test_get_rooms():
    response = client.get("/api/v1/rooms")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# 2. Ошибка 404 при бронировании несуществующей категории
def test_create_booking_invalid_room():
    payload = {
        "room_tier": "non_existent_tier",
        "check_in": str(date.today() + timedelta(days=1)),
        "check_out": str(date.today() + timedelta(days=3)),
        "guests": 2,
        "full_name": "Тест Тестов",
        "email": "test@example.com",
        "phone": "+77001112233"
    }
    response = client.post("/api/v1/bookings", json=payload)
    assert response.status_code == 404
    assert "не найдена" in response.json()["detail"]


# 3. Ошибка валидации Pydantic (выезд раньше заезда)
def test_create_booking_invalid_dates():
    payload = {
        "room_tier": "deluxe",
        "check_in": str(date.today() + timedelta(days=5)),
        "check_out": str(date.today() + timedelta(days=2)),  # Дата выезда раньше заезда
        "guests": 1,
        "full_name": "Тест Тестов",
        "email": "test@example.com",
        "phone": "+77001112233"
    }
    response = client.post("/api/v1/bookings", json=payload)
    assert response.status_code == 422  # Validation Error


# 4. Успешное создание брони и проверка расчета стоимости
def test_create_booking_success():
    payload = {
        "room_tier": "deluxe",
        "check_in": str(date.today() + timedelta(days=10)),
        "check_out": str(date.today() + timedelta(days=12)),  # 2 ночи
        "guests": 2,
        "full_name": "Иван Иванов",
        "email": "ivan@example.com",
        "phone": "+77079998877",
        "special_requests": "Тихий номер"
    }
    response = client.post("/api/v1/bookings", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["status"] == "pending"
    assert data["total_price"] == 145000 * 2  # 145 000 тг/ночь * 2 ночи


# 5. Изменение статуса созданного бронирования
def test_update_booking_status():
    # Создаем бронь
    payload = {
        "room_tier": "deluxe",
        "check_in": str(date.today() + timedelta(days=20)),
        "check_out": str(date.today() + timedelta(days=21)),
        "guests": 1,
        "full_name": "Петр Петров",
        "email": "petr@example.com",
        "phone": "+77075554433"
    }
    create_res = client.post("/api/v1/bookings", json=payload)
    booking_id = create_res.json()["id"]

    # Меняем статус на confirmed
    patch_res = client.patch(
        f"/api/v1/bookings/{booking_id}/status", 
        json={"status": "confirmed"}
    )
    assert patch_res.status_code == 200
    assert patch_res.json()["status"] == "confirmed"