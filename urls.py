from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('weather', views.weather_view, name='weather'),
    path('weather_form/', views.weather_form, name='weather_form'),
    path('weather_search/', views.weather_search, name='weather_search'),
    path('weather_search_by_coordinates/', views.weather_search_by_coordinates, name='weather_search_by_coordinates'),
]























