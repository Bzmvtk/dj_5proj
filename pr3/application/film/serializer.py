from rest_framework import serializers

from application.film.models import Film


class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'