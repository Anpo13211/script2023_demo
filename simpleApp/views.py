from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from asgiref.sync import async_to_sync
import httpx
import datetime
import pytz
import requests
from . import weather

API_KEY = 'f3e728115fcccee554aee016426b7e34'
CITY_NAME = 'Tokyo'
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

params = {
    'q': CITY_NAME,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ja'
}

# Tokyo's coordinates
default_lat = '35.69'
default_lon = '139.69'



def weather_search_by_coordinates(request):
    lat = request.GET.get('lat', default_lat)
    lon = request.GET.get('lon', default_lon)
    current = async_to_sync(weather.search_weather_by_coordinates)(lat, lon)
    forecast = async_to_sync(weather.search_forecast_by_coordinates)(lat, lon)

    now = datetime.datetime.now()
    if forecast:
        for entry in forecast['list']:
            entry['dt_txt'] = convert_utc_to_local(entry['dt_txt'])

    if current['city'] == '堀ノ内':
        current['city'] = 'Tokyo'
        forecast['city']['name'] = 'Tokyo'

    context = {
        'forecast': forecast,
        'current': current,
        'current_time': now
    }
    return render(request, 'forecast.html', context)


def convert_utc_to_local(utc_dt_str):
    utc_dt = datetime.datetime.strptime(utc_dt_str, '%Y-%m-%d %H:%M:%S')
    utc_dt = pytz.utc.localize(utc_dt)

    local_tz = pytz.timezone('Asia/Tokyo')
    local_dt = utc_dt.astimezone(local_tz)

    return local_dt.strftime('%Y-%m-%d %H:%M:%S')

def weather_view(request):
    lat = request.GET.get('lat', default_lat)
    lon = request.GET.get('lon', default_lon)
    current = async_to_sync(weather.search_weather_by_coordinates)(lat, lon)
    forecast = async_to_sync(weather.search_forecast_by_coordinates)(lat, lon)

    now = datetime.datetime.now()

    if forecast:  # Only if forecast data exists
        for entry in forecast['list']:
            entry['dt_txt'] = convert_utc_to_local(entry['dt_txt'])

    if current['city'] == '堀ノ内':
        current['city'] = 'Tokyo'
        forecast['city']['name'] = 'Tokyo'

    context = {
        'forecast': forecast,
        'current': current,
        'current_time': now
    }
    return render(request, 'forecast.html', context)


def weather_form(request):
    return render(request, 'search_form.html')

def weather_search(request):
    city = request.GET.get('city', CITY_NAME)
    forecast = async_to_sync(weather.search_forecast)(city)
    current = async_to_sync(weather.search_weather)(city)

    now = datetime.datetime.now()
    if forecast:
        for entry in forecast['list']:
            entry['dt_txt'] = convert_utc_to_local(entry['dt_txt'])

    context = {
        'city': city,
        'forecast': forecast,
        'current': current,
        'current_time': now
    }
    return render(request, 'search.html', context)
