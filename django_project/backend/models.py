from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Team(models.Model):
    players = models.ManyToManyField(Player)


class Game(models.Model):
    date = models.DateField()
    teams = models.ManyToManyField(Team)


class StatType(models.Model):
    name = models.CharField(max_length=200)


class Stat(models.Model):
    type = models.ForeignKey(StatType, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    value = models.IntegerField()
