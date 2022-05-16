from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_calc(self):
        """ a test to add two numbers """
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        """ a test to subtract two numbers """
        self.assertEqual(subtract(1, 1), 0)
