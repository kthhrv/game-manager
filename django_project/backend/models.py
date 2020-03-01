from django.db import models
from django.utils.html import format_html


class Player(models.Model):
    name = models.CharField(max_length=200)
    ringer = models.BooleanField(default=False)
    email = models.EmailField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Team(models.Model):
    players = models.ManyToManyField(Player)
    goals = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Game(models.Model):
    date = models.DateField(unique=True)
    players = models.ManyToManyField(Player, blank=True)
    team_a = models.ForeignKey(Team, 
        on_delete=models.CASCADE, 
        related_name='game_team_a',
        null=True,
    )
    team_b = models.ForeignKey(Team, 
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        team_a = Team()
        team_a.save()
        team_b = Team()
        team_b.save()
        self.team_a = team_a
        self.team_b = team_b
        super().save(*args, **kwargs)

    def get_score(self):
        return f'{ self.team_a.goals } - { self.team_b.goals }'

    def get_players_count(self):
        return len(self.players.all())

    def display_team_a_players(self):
        if self.team_a:
            return format_html('<br>'.join(str(p) for p in self.team_a.players.all()))
        else:
            return

    def display_team_b_players(self):
        if self.team_b:
            return format_html('<br>'.join(str(p) for p in self.team_b.players.all()))
        else:
            return



class StatType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Stat(models.Model):
    stat_type = models.ForeignKey(StatType, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return str(self.stat_type.name)
