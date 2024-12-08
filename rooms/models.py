from django.db import models

from django.conf import settings
from django.db.models import Avg


# C:\Users\Lenovo\Desktop\мидкаджанго\Qosyl\rooms\models.py

class Room(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey('users.Topic', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def average_rating(self):
        return Rating.objects.filter(room=self).aggregate(Avg('rating'))['rating__avg'] or 0


    def __str__(self):
        return f'{self.name}: {self.average_rating()}'

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.room.name}: {self.rating}'