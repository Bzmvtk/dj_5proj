from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

class Type(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

class Car(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=None)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')

    def __str__(self):
        return f'{self.brand} {self.title}\n {self.year}'