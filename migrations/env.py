import sys
from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import engine_from_config, pool
from alembic import context

# 1. Добавляем путь к корню проекта, чтобы Alembic видел папку app
sys.path.append(str(Path(__file__).resolve().parents[1]))

# 2. Импортируем Base, URL базы и ВСЕ модели
from app.database import Base, SQLALCHEMY_DATABASE_URL
from app.models import Room, Booking  # noqa

# Конфигурация Alembic
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 3. Передаем метаданные наших моделей в Alembic
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Запуск миграций в оффлайн-режиме."""
    url = SQLALCHEMY_DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме."""
    configuration = config.get_section(config.config_ini_section, {})
    # Подставляем наш URL из .env
    configuration["sqlalchemy.url"] = SQLALCHEMY_DATABASE_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()