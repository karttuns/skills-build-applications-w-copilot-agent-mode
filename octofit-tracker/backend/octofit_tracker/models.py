from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=32, null=True)

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=32)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()

class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

class Leaderboard(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=32)
    points = models.IntegerField()