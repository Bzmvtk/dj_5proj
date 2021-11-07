from django.urls import path

from application.game.views import GameListView

urlpatterns = [
    path('game-list/', GameListView.as_view()),
]