from rest_framework import serializers

from application.car.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'