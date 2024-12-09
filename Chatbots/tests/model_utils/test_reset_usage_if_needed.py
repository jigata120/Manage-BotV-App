from django.test import TestCase
from unittest.mock import patch
from django.utils.timezone import datetime, make_aware
from Chatbots.models import Usage
from Chatbots.model_utils import reset_usage_if_needed


class ResetUsageTestCase(TestCase):
    def setUp(self):
        self.usage_1 = Usage.objects.create(
            updated_at=make_aware(datetime(2024, 12, 9, 23, 59)),
            daily_interactions=10,
            daily_tokens_usage=500,
            monthly_interactions=100,
            monthly_tokens_usage=5000,
        )
        self.usage_2 = Usage.objects.create(
            updated_at=make_aware(datetime(2024, 12, 1, 0, 0)),
            daily_interactions=5,
            daily_tokens_usage=200,
            monthly_interactions=50,
            monthly_tokens_usage=3000,
        )

    @patch("Chatbots.model_utils.timezone.now")
    def test_reset_usage_if_needed(self, mock_now):
        mock_now.return_value = make_aware(datetime(2024, 12, 10, 12, 0))
        reset_applied = reset_usage_if_needed()

        self.assertTrue(reset_applied)

        # Refresh the objects to see updates
        self.usage_1.refresh_from_db()
        self.usage_2.refresh_from_db()

        self.assertEqual(self.usage_1.daily_interactions, 0)
        self.assertEqual(self.usage_1.daily_tokens_usage, 0)
        self.assertEqual(self.usage_2.daily_interactions, 0)
        self.assertEqual(self.usage_2.daily_tokens_usage, 0)

        # Monthly values remain unchanged unless it's the first of the month
        self.assertEqual(self.usage_1.monthly_interactions, 100)
        self.assertEqual(self.usage_2.monthly_interactions, 50)
