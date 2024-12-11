from django.test import TestCase

from users.models import User
import pytest

@pytest.mark.django_db
def test_default_is_active():
    user = User.objects.create_user(username="testuser", password="12345" , email="test@gmail.com")
    assert user.is_active is True  # Assuming that is_active defaults to True
