import unittest
from dates import check_date
from datetime import date


class MyTestClass(unittest.TestCase):
    def test_check_date(self):
        self.assertTrue(check_date(date(1998, 11, 15)), "something wrong")
        self.assertFalse(check_date(date(3000, 11, 15)))