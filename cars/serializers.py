from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'date_on_yard', 'style', 'drive_type', 'engine', 'fuel_type', 'vin', 'color', 'transmission']