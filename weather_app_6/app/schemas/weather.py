from pydantic import BaseModel, Field
from typing import Optional

class WeatherRequest(BaseModel):
    city: Optional[str] = Field(default=None, description="Название города")
    lat: Optional[float] = Field(default=None, description="Широта")
    lon: Optional[float] = Field(default=None, description="Долгота")

    # Минимальная валидация: нужно либо city, либо координаты
    def validate_query(self):
        if not self.city and (self.lat is None or self.lon is None):
            raise ValueError("Нужно указать либо город, либо координаты.")