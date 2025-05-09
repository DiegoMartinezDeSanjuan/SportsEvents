from django.db import models
from django.contrib.auth.models import User

class SportsEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    sport_type = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')


    def __str__(self):
        return f"{self.name} ({self.date})"


class Team(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=100)
    events = models.ManyToManyField(SportsEvent, related_name='teams')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')


    def __str__(self):
        return f"{self.name} - {self.country}"


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='athletes')
    events = models.ManyToManyField(SportsEvent, related_name='athletes')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='athletes')

    def __str__(self):
        return self.name
