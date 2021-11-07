from django.contrib import admin

from application.car.models import Brand, Type, Car

admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Car)