from django.db import models
from django.contrib.auth.models import AbstractUser
# C:\Users\Lenovo\Desktop\мидкаджанго\Qosyl\users\models.py

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


