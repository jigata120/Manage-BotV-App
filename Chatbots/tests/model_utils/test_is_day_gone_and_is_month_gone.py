from django.test import TestCase
from unittest.mock import patch
from django.utils.timezone import datetime, make_aware
from Chatbots.model_utils import is_day_gone, is_month_gone  # Adjust import path accordingly


class TimeFunctionsTestCase(TestCase):
    @patch("Chatbots.model_utils.timezone.now")
    def test_is_day_gone(self, mock_now):
        mock_now.return_value = make_aware(datetime(2024, 12, 10, 12, 0))
        last_updated = make_aware(datetime(2024, 12, 9, 23, 59))
        self.assertTrue(is_day_gone(last_updated))

        last_updated = make_aware(datetime(2024, 12, 10, 0, 0))
        self.assertFalse(is_day_gone(last_updated))

    @patch("Chatbots.model_utils.timezone.now")
    def test_is_month_gone(self, mock_now):
        mock_now.return_value = make_aware(datetime(2024, 12, 10, 12, 0))
        last_updated = make_aware(datetime(2024, 11, 30, 23, 59))
        self.assertTrue(is_month_gone(last_updated))

        last_updated = make_aware(datetime(2024, 12, 1, 0, 0))
        self.assertFalse(is_month_gone(last_updated))
