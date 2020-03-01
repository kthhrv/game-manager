from django.contrib import admin
from backend.models import Player, Team, Game, StatType, Stat

admin.site.register(Player)
admin.site.register(Team)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = (
        'date',
        'players',
    )
    list_display = (
        'date',
        'get_players_count',
        'get_score',
        'display_team_a_players',
        'display_team_b_players',
    )


admin.site.register(StatType)


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = (
        'stat_type',
        'game',
        'player',
        'value',
    )
    list_filter = (
        'stat_type',
        'game',
        'player',
    )
