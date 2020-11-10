import unittest
from src.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.temp = User()
    