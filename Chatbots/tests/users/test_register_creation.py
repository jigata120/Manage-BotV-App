from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from Chatbots.models import Chatbot, Settings, Usage, ContextData

User = get_user_model()


class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(
            reverse("register"),
            data={
                "username": "testuser",
                "email": "testuser@example.com",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        user = User.objects.filter(username="testuser").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "testuser@example.com")

        chatbot = Chatbot.objects.filter(user=user).first()
        self.assertIsNotNone(chatbot)
        self.assertEqual(chatbot.name, "testuser's Free Chatbot")
        self.assertEqual(chatbot.description, "Free Trial Chatbot.")

        self.assertIsNotNone(chatbot.settings)
        self.assertIsNotNone(chatbot.usage)
        self.assertIsNotNone(chatbot.settings.context_data)

    def test_user_registration_invalid_data(self):
        response = self.client.post(
            reverse("register"),
            data={
                "username": "testuser",
                "email": "testuser@example.com",
                "password1": "password123",
                "password2": "password456", 
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match.")
        self.assertFalse(User.objects.filter(username="testuser").exists())

    def test_user_registration_creates_single_chatbot(self):
        """Ensure only one chatbot is created for a user during registration."""
        response = self.client.post(
            reverse("register"),
            data={
                "username": "testuser",
                "email": "testuser@example.com",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
            },
        )

        self.assertEqual(response.status_code, 302)
        user = User.objects.filter(username="testuser").first()

        chatbots = Chatbot.objects.filter(user=user)
        self.assertEqual(chatbots.count(), 1)

    def test_chatbot_settings_and_usage(self):
        """Ensure chatbot settings and usage are associated properly."""
        response = self.client.post(
            reverse("register"),
            data={
                "username": "testuser",
                "email": "testuser@example.com",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
            },
        )

        self.assertEqual(response.status_code, 302)
        user = User.objects.filter(username="testuser").first()
        chatbot = Chatbot.objects.filter(user=user).first()

        self.assertIsNotNone(chatbot.settings)
        self.assertIsNotNone(chatbot.usage)
        self.assertIsInstance(chatbot.settings, Settings)
        self.assertIsInstance(chatbot.usage, Usage)

        self.assertIsNotNone(chatbot.settings.context_data)
        self.assertIsInstance(chatbot.settings.context_data, ContextData)
