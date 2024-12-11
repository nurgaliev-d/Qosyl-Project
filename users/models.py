from django.db import models
from django.utils import timezone
from chat.models import Message
from django.contrib.auth.models import AbstractUser
from rooms.models import Room
from django.db.models import Q


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
    
    def is_friend(self, user1, user2):
        return Friendship.objects.filter(
            (Q(user1=user1) & Q(user2=user2)) |
            (Q(user1=user2) & Q(user2=user1))
        ).exists()

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(upload_to='avatars/', default='avatar.svg')
    friends = models.ManyToManyField('self', symmetrical=False, related_name='friends_with', blank=True)

    def is_friend(self, user):
        return self.friends.filter(id=user.id).exists()
    
    def send_friend_request(self, user):
        if not self.is_friend(user):
            FriendRequest.objects.get_or_create(from_user=self, to_user=user)

    def accept_friend_request(self, user):
        if not self.is_friend(user):
            self.friends.add(user)
            user.friends.add(self)
            FriendRequest.objects.filter(from_user=user, to_user=self).delete()

    def remove_friend(self, user):
        self.friends.remove(user)
        user.friends.remove(self)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)


    def accept(self):
        self.from_user.accept_friend_request(self.to_user)
        self.accepted = True
        self.save()

    def reject(self):
        self.delete()

    def __str__(self):
        return f"{self.from_user.username} -> {self.to_user.username}"

    def save(self, *args, **kwargs):
        # Prevent a user from sending a friend request to themselves
        if self.from_user == self.to_user:
            raise ValueError("You cannot send a friend request to yourself.")
        super().save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['room']),
            models.Index(fields=['timestamp']),
        ]

    def __str__(self):
        return f"{self.user.username} commented in {self.room.name} at {self.timestamp}"
        
class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='friendship_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friendship_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1} & {self.user2}"

    # Ensures only one friendship record exists for two users
    class Meta:
        unique_together = ('user1', 'user2')
