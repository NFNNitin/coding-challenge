from .models import Weather, Yield,Weather_stats
from rest_framework import serializers 

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = "__all__"

class YieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yield
        fields = "__all__"

class WeatherStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather_stats
        fields = "__all__"
    