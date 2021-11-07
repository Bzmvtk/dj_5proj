from django.contrib import admin

from application.book.models import Genre, Country, Book

admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Book)
