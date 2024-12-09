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
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(upload_to='avatars/', default='avatar.svg')
    friends = models.ManyToManyField('self', blank=True, symmetrical=True, related_name='user_friends')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def add_friend(self, friend):
        """Adds a friend to the user's friends list."""
        if friend != self and not self.friends.filter(id=friend.id).exists():
            self.friends.add(friend)

    def remove_friend(self, friend):
        """Removes a friend from the user's friends list."""
        if self.friends.filter(id=friend.id).exists():
            self.friends.remove(friend)

    def is_friend(self, friend):
        """Checks if the user is friends with another user."""
        return self.friends.filter(id=friend.id).exists()


    objects = UserManager()

    
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def accept(self):
        """Accept the friend request."""
        self.from_user.add_friend(self.to_user)
        self.to_user.add_friend(self.from_user)
        self.delete()

    def decline(self):
        """Decline the friend request."""
        self.delete()

    def __str__(self):
        return f"{self.from_user} → {self.to_user}"

    def save(self, *args, **kwargs):
        # Prevent a user from sending a friend request to themselves
        if self.from_user == self.to_user:
            raise ValueError("You cannot send a friend request to yourself.")
        super().save(*args, **kwargs)