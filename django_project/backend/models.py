from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)
    ringer = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Team(models.Model):
    side = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.side


class Game(models.Model):
    date = models.DateField(unique=True)
    players = models.ManyToManyField(Player, blank=True)
    teams = models.ManyToManyField(Team)


class StatType(models.Model):
    name = models.CharField(max_length=200)


class Stat(models.Model):
    type = models.ForeignKey(StatType, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    value = models.IntegerField()
