from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Country(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=None)
    Author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='book')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')

    def __str__(self):
        return f'{self.title} {self.Author}\n {self.genre} {self.country}'