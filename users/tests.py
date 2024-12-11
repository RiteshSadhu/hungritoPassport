from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser, Profile

class UserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            whatsapp_number='+1234567890'
        )

    def test_login_view(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_authenticated(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_unauthenticated(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)