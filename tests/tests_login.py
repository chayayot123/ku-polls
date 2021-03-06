"""Tests of authentication."""
import django.test
from django.urls import reverse
from django.contrib.auth.models import User


class UserAuthTest(django.test.TestCase):

    def setUp(self):
        super().setUp()
        self.username = "testuser"
        self.password = "Fat-Chance!"
        self.user1 = User.objects.create_user(
                         username=self.username,
                         password=self.password,
                         email="testuser@nowhere.com")
        self.user1.first_name = "Tester"
        self.user1.save()

    def test_login_view(self):
        """Test that a user can login via the login view."""
        login_url = reverse("login")
        response = self.client.get(login_url)
        self.assertEqual(200, response.status_code)
        form_data = {"username": "testuser", "password": "Fat-Chance!"}
        response = self.client.post(login_url, form_data)
        self.assertEqual(302, response.status_code)
        # should redirect us to the polls index page ("polls:index")
        self.assertRedirects(response, reverse("polls:index"))