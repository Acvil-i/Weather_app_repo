from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api import weather
import os

load_dotenv()

print(os.getenv("WEATHER_API_URL"))
print(os.getenv("WEATHERAPI_KEY"))

app = FastAPI()

# Регистрируем роутер /weather
app.include_router(weather.router)