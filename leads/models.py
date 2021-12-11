from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#   pass



class Lead(models.Model):
  fristName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  email = models.EmailField(max_length=50)
  def __str__(self) -> str:
      return self.fristName + " " + self.lastName
      