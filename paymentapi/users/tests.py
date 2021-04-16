from rest_framework.test import APITestCase
from django.urls import reverse


# Create your tests here.

class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse("users:create_user")

    def test_invalid_credentials(self):
        user_data = {
            "username": "kojo",
            "password": "kojo@gmail.com",
            "confirm_password": "Wrong Password"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)
