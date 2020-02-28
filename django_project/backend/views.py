from backend.models import Player, Game
from rest_framework import viewsets
from backend.serializers import PlayerSerializer, GameSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('date')
    serializer_class = GameSerializer
