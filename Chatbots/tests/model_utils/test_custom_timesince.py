from django.test import TestCase
from django.utils.timezone import datetime, make_aware
from Chatbots.model_utils import custom_timesince
from unittest.mock import patch


class CustomTimesinceTestCase(TestCase):
    def test_custom_timesince_days(self):
        updated_at = make_aware(datetime(2024, 12, 8, 12, 0))
        now = make_aware(datetime(2024, 12, 10, 12, 0))
        with patch("Chatbots.model_utils.now", return_value=now):
            self.assertEqual(custom_timesince(updated_at), "2 days ago")

    def test_custom_timesince_hours(self):
        updated_at = make_aware(datetime(2024, 12, 10, 10, 0))
        now = make_aware(datetime(2024, 12, 10, 12, 0))
        with patch("Chatbots.model_utils.now", return_value=now):
            self.assertEqual(custom_timesince(updated_at), "2 hours ago")

    def test_custom_timesince_minutes(self):
        updated_at = make_aware(datetime(2024, 12, 10, 11, 55))
        now = make_aware(datetime(2024, 12, 10, 12, 0))
        with patch("Chatbots.model_utils.now", return_value=now):
            self.assertEqual(custom_timesince(updated_at), "5 minutes ago")

    def test_custom_timesince_seconds(self):
        updated_at = make_aware(datetime(2024, 12, 10, 11, 59, 50))
        now = make_aware(datetime(2024, 12, 10, 12, 0))
        with patch("Chatbots.model_utils.now", return_value=now):
            self.assertEqual(custom_timesince(updated_at), "10 seconds ago")
