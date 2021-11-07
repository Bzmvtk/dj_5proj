from rest_framework import generics

from application.car.models import Car
from application.car.serializer import CarSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer