# 🏨 Hotel Booking System REST API

A full-stack asynchronous web application for booking hotel rooms, built with **FastAPI**, **SQLite/PostgreSQL**, and containerized with **Docker**.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat&logo=docker)
![Pytest](https://img.shields.io/badge/Tests-Pytest-yellow?style=flat&logo=pytest)

---

## ✨ Features

- **Asynchronous Architecture:** High-performance REST API powered by FastAPI & Uvicorn.
- **Room Booking Management:** API endpoints for filtering available rooms, creating, and canceling reservations.
- **Data Validation:** Strict schema validation powered by Pydantic.
- **Database Migrations:** Schema control using Alembic.
- **Automated Testing:** Unit & integration test coverage via `pytest`.
- **Frontend Interface:** Lightweight Web UI (HTML/JS/CSS) integrated with backend endpoints.
- **Dockerized Setup:** Ready-to-deploy container setup with `docker-compose`.

---

## 🛠 Tech Stack

- **Backend:** Python 3.11, FastAPI, Uvicorn
- **Database & ORM:** SQLite / PostgreSQL, SQLAlchemy, Alembic
- **Testing:** Pytest
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **DevOps:** Docker, Docker Compose

---

## 🚀 Quick Start (Docker)

Run the entire application in a container with a single command:

```bash
docker-compose up --build
