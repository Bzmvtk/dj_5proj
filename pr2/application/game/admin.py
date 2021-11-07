from django.contrib import admin

from application.game.models import Genre, Platform, Game

admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Game)
