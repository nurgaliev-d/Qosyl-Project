# C:\Users\Lenovo\Desktop\Qosyl-Project\tests\test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="testuser@example.com", password="password123")
        self.client.login(email="testuser@example.com", password="password123")
    
 
    # def test_user_detail(self):
    #     # Test GET request to retrieve a single user's details
    #     response = self.client.get(f'/api/users/{self.user.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['id'], self.user.id)

    # def test_create_user(self):
    #     # Test POST request to create a new user
    #     response = self.client.post('/api/users/', {
    #         'email': 'newuser@example.com',
    #         'password': 'password123',
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data['email'], 'newuser@example.com')
