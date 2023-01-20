"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModulTests(TestCase):
    """ Test models"""

    def test_create_user_with_email_successful(self):
        expected = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=expected,
            password=password
        )

        self.assertEqual(user.email, expected)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['TEST4@EXAMPLE.COM', 'TEST4@example.com'],
        ]

        for emai, expected in sample_emails:
            user = get_user_model().objects.create_user(emai, 'sample123')
            self.assertEqual(user.email, expected)
