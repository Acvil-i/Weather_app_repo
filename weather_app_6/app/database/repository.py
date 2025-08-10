from sqlalchemy.orm import Session
from app.database.models import WeatherRequest as WeatherRequestModel
from app.schemas.weather import WeatherRequest as WeatherRequestSchema

def save_weather_request(
    session: Session,
    query: WeatherRequestSchema,
    result: dict
):
    # Формируем модель для сохранения
    db_record = WeatherRequestModel(
        city=query.city,
        lat=query.lat,
        lon=query.lon,
        temperature=result["температура"]  # ожидаем ключ
    )

 
    session.add(db_record)
    session.commit()
