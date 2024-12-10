from django.db import models
from django.contrib.auth.models import AbstractUser
# C:\Users\Lenovo\Desktop\мидкаджанго\Qosyl\users\models.py

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True,unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


class MyChats(models.Model):
    me = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='it_me')
    frnd = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='my_frnd')
    chats = models.JSONField(default=dict)


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


