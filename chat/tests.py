from django.test import TestCase
from .models import Message
from users.models import User
from rooms.models import Room 

import pytest
@pytest.mark.django_db
def test_message_creation():
    user = User.objects.create_user(email="testuser@example.com", password="12345")
    room = Room.objects.create(name="Test Room")  
    message = Message.objects.create(user=user, room=room, body="Hello World!")
    
    assert message.body == "Hello World!"
    assert message.user == user
    assert message.room == room

