from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('weather.html', views.weather, name='weather'),
    path('index.html', views.index, name='home')
]