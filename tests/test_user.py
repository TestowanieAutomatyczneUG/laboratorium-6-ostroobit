import unittest
from src.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.temp = User()
    
    def test_single_character(self):
        self.assertEqual(self.temp.valid_password("a"), False)