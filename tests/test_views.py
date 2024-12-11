# C:\Users\Lenovo\Desktop\Qosyl-Project\tests\test_views.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rooms.models import Room
from chat.models import Message
from users.models import User
from django.shortcuts import get_object_or_404

class ChatRoomViewTest(TestCase):
    def setUp(self):
        # Provide an email field along with the username and password
        self.user1 = User.objects.create_user(username='user1', password='password', email='user1@example.com')
        self.user2 = User.objects.create_user(username='user2', password='password', email='user2@example.com')
        self.room = Room.objects.create(name='Test Room')
