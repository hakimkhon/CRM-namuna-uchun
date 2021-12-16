from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
  pass

class Lead(models.Model):
  fristName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  email = models.EmailField(max_length=50)
  agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
  def __str__(self):
      return self.fristName + " " + self.lastName
class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.user)