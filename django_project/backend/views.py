from backend.models import Player, Team, Game
from rest_framework import viewsets
from backend.serializers import PlayerSerializer, TeamSerializer, GameSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('id')
    serializer_class = TeamSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('date')
    serializer_class = GameSerializer
