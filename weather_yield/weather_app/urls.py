from django.urls import path
from .views import WeatherList, Yield, Stats
urlpatterns = [
    path('weather/', WeatherList.as_view(), name='weather'),
    path("yield/", Yield.as_view(), name='yield'),
    path("weather/stats", Stats.as_view(), name='weather_stats')
    ]