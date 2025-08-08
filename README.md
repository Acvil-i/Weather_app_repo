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
  
## Добавить .env в корень проекта 
- POSTGRES_USER=postgres  *Имя пользователя БД
- POSTGRES_PASSWORD=postgres *Пароль пользователя БД
- POSTGRES_DB=weather_db *Название БД к которой мы будем подключаться
- POSTGRES_HOST=localhost *Адрес подключения
- POSTGRES_PORT=5433 *Порт
- WEATHER_API_URL=https://api.weatherapi.com/v1/current.json *Ссылка по которой делается запрос
- WEATHERAPI_KEY=cb837c081df748578b0101844250608 *Ключик буратино


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
