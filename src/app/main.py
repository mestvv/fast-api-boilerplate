from fastapi import FastAPI
from .routers import user
from .database import Base, engine

app = FastAPI()

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Подключаем роутеры
app.include_router(user.router)
