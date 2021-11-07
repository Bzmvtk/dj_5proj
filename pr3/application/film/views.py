from rest_framework import generics

from application.film.models import Film
from application.film.serializer import FilmSerializers


class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
