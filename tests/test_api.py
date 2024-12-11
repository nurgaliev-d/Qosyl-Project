import pytest
from rooms.models import Room
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_room_creation():
    room = Room.objects.create(name="Test Room", description="Test Description")
    assert room.name == "Test Room"
    assert room.description == "Test Description"
