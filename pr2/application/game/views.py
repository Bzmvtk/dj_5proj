from rest_framework import generics

from application.game.models import Game
from application.game.serializer import GameSerializers


class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers