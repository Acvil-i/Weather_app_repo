from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Создаём базовый класс для модели SQLAlchemy
Base = declarative_base()

class WeatherRequest(Base):
    __tablename__ = "weather_requests"  # имя таблицы в БД

    id = Column(Integer, primary_key=True, index=True)  # первичный ключ
    city = Column(String, nullable=True)                 # название города
    lat = Column(Float, nullable=True)                   # широта
    lon = Column(Float, nullable=True)                   # долгота
    temperature = Column(Float)                          # сохранённая температура
    timestamp = Column(DateTime, default=datetime.utcnow) # время запроса, сохраняем UTC