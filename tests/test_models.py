# tests/test_models.py
from django.test import TestCase
from chat.models import Message

from users.models import User

from rooms.models import Room

class MessageModelTest(TestCase):
    def setUp(self):
        # Create a user and a room
        self.user = User.objects.create_user(username='testuser', password='password', email="test@gmail.com")
        self.room = Room.objects.create(name='Test Room')

    def test_message_str(self):
        # Create a message and check if the string representation works
        message = Message.objects.create(user=self.user, room=self.room, body="Test message")
        self.assertEqual(str(message), 'Test message')  # First 50 characters of body
