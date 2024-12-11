from rooms.models import Room
import pytest

@pytest.mark.django_db
def test_null_field():
    room = Room.objects.create(name="Test Room", description=None)
    assert room.description is None  # Ensure that null value is allowed if it's configured


@pytest.mark.django_db
def test_room_method():
    room = Room.objects.create(name="Test Room", description="A nice room")
    assert room.name == "Test Room"  # Assuming a method get_room_info() exists
