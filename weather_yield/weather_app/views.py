from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import WeatherSerializer, YieldSerializer, WeatherStatsSerializer
from .models import Weather, Yield, Weather_stats

class WeatherList(generics.ListAPIView):
    """
    """
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()

class Yield(generics.ListAPIView):
    """
    """
    serializer_class = YieldSerializer
    queryset = Yield.objects.all()

class Stats(generics.ListAPIView):
    """
    """
    serializer_class = WeatherStatsSerializer
    queryset = Weather_stats.objects.all()