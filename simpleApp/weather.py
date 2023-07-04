import httpx
import datetime

API_KEY = 'f3e728115fcccee554aee016426b7e34'
CITY_NAME = 'Tokyo'
BASE_URL_FORECAST = "http://api.openweathermap.org/data/2.5/forecast"
BASE_URL_CURRENT = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q': CITY_NAME,
    'appid': API_KEY,
    'units': 'metric',  # Use 'imperial' for Fahrenheit
    'lang': 'ja',
    'cnt': 12
}

async def search_fetch_forecast(session, url, city):
    params['q'] = city
    response = await session.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

async def search_current_weather(session, url, city):
    params['q'] = city
    response = await session.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_data
    else:
        return None
    
async def search_current_weather_by_coordinates(session, url, lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
        'lang': 'ja',
    }
    response = await session.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_data
    else:
        return None


async def search_fetch_forecast_by_coordinates(session, url, lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
        'lang': 'ja',
        'cnt': 12
    }
    response = await session.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None



async def search_forecast_by_coordinates(lat, lon):
    async with httpx.AsyncClient() as client:
        return await search_fetch_forecast_by_coordinates(client, BASE_URL_FORECAST, lat, lon)

async def search_weather_by_coordinates(lat, lon):
    async with httpx.AsyncClient() as client:
        return await search_current_weather_by_coordinates(client, BASE_URL_CURRENT, lat, lon)

async def search_forecast(city):
    async with httpx.AsyncClient() as client:
        return await search_fetch_forecast(client, BASE_URL_FORECAST, city)

async def search_weather(city):
    async with httpx.AsyncClient() as client:
        return await search_current_weather(client, BASE_URL_CURRENT, city)
