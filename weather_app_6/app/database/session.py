import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_HOST = os.getenv("POSTGRES_HOST", "db")         # в контейнере — сервис 'db'
DB_PORT = os.getenv("POSTGRES_PORT", "5432")       # в контейнере postgres слушает 5432
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_NAME = os.getenv("POSTGRES_DB", "weather_db")

# Формируем URL для SQLAlchemy (psycopg2)
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаём движок и SessionLocal
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Зависимость для FastAPI — генератор с контекстом
def get_session():
    with SessionLocal() as session:
        yield session