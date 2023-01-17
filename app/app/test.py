from django.test import SimpleTestCase

from app import calc


class Calctest(SimpleTestCase):
    def test_add_number(self):
        res = calc.calc(5, 8)
        self.assertEqual(res, 13)
