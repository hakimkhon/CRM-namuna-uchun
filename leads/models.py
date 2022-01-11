from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
  pass

class UserProfil(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
      return str(self.user.username)

class Lead(models.Model):
  fristName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  email = models.EmailField(max_length=50)
  agent = models.ForeignKey("Agent", blank = True, on_delete=models.CASCADE)
  def __str__(self):
      return self.fristName

class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profil = models.ForeignKey(UserProfil, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.user)

class Userlar(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profil = models.ForeignKey(UserProfil, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.user)

def post_user_yaratish(sender, instance, created, **kwargs):
  if created:
    UserProfil.objects.create(user = instance)

post_save.connect(post_user_yaratish, sender = User)