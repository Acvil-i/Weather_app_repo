from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
# Импортируем сервисы получения погоды
from app.services.weather_service import get_weather_by_city, get_weather_by_coordinates
# Импортируем pydantic-схему
from app.schemas.weather import WeatherRequest
from app.database.session import get_session
from app.database.repository import save_weather_request

router = APIRouter()

@router.post("/weather")
def weather(query: WeatherRequest, db: Session = Depends(get_session)):
    try:
        # Валидируем входные данные
        query.validate_query()
        print("Получен запрос на /weather")
        print("Данные:", query)

        if query.city:
            result = get_weather_by_city(query.city)
        else:
            result = get_weather_by_coordinates(query.lat, query.lon)

        # Сохраняем запрос в БД
        save_weather_request(db, query, result)

        # Возвращаем результат пользователю
        return result

    except ValueError as ve:
        # Неправильные входные данные — 400
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # Общая ошибка — 500
        print("Ошибка при обработке запроса:", str(e))
        raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера.")