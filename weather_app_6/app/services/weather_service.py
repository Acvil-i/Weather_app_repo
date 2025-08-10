from dotenv import load_dotenv
load_dotenv()

import os
import httpx

# Конфигурация API (берётся из .env)
WEATHER_API_URL = os.getenv("WEATHER_API_URL")
WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY")


print("API URL:", WEATHER_API_URL)

def get_weather_by_city(city: str):
    params = {
        "key": WEATHERAPI_KEY,
        "q": city,
        "lang": "ru"
    }
    return _fetch_weather(params)

def get_weather_by_coordinates(lat: float, lon: float):
    coords = f"{lat},{lon}"
    params = {
        "key": WEATHERAPI_KEY,
        "q": coords,
        "lang": "ru"
    }
    return _fetch_weather(params)

def _fetch_weather(params: dict):
    # Запрос к внешнему API
    print(f"Отправляем запрос: {WEATHER_API_URL}, параметры: {params}")
    with httpx.Client() as client:
        response = client.get(WEATHER_API_URL, params=params)
        print(f"Ответ от API: {response.status_code}")
        if response.status_code != 200:
            raise Exception(f"Ошибка при обращении к WeatherAPI: {response.text}")

        data = response.json()
        return {
            "город": data["location"]["name"],
            "температура": data["current"]["temp_c"],
            "описание": data["current"]["condition"]["text"]
        }
