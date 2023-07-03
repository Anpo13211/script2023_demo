from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hi', views.hi, name='hi'),
    path('hi/<str:someone>', views.greet, name='greet'),
]