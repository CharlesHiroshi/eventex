from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Charles Hiroshi',
            cpf = '12345678901',
            email = 'charles_hiroshi@wttd.com',
            phone = '99-9999-9999'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists)

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Charles Hiroshi', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must False"""
        self.assertEqual(False, self.obj.paid)