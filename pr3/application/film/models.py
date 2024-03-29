from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Studio(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Film(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField(default=2000)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='film')
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='studio')

    def __str__(self):
        return f'{self.title} {self.year}\n {self.genre} {self.studio}'
