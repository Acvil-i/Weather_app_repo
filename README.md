Weather_app

## Описание
Приложение возвращает текущую погоду по названию города или по координатам (lat, lon). Входные запросы сохраняются в базу данных.

## Стек
- FastAPI, Pydantic
- SQLAlchemy
- Alembic
- PostgreSQL (в Docker)
- Docker / docker-compose
- httpx (внешний запрос к WeatherAPI)

## Как запустить проект
-```bash
git clone https://github.com/USERNAME/weather_app.git
cd weather_app

-Запустить проект в Docker
 docker compose -f docker-compose.yml up --build -d
 Swagger UI (документация API) доступен на http://localhost:8000/docs

-Настройка миграции
 Создать миграцию:docker-compose exec web alembic revision --autogenerate -m "init"
 Применить миграцию:docker-compose exec web alembic upgrade head
