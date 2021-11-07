from django.contrib import admin

from application.film.models import Genre, Studio, Film

admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Film)