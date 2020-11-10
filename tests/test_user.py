import unittest
from src.user import User


class TeshtUser(unittest.TestCase):
    def setUp(self):
        self.temp = User()
    
    def test_single_character(self):
        self.assertEqual(self.temp.valid_password("a"), False)
    
    def test_less_than_8_letters(self):
        self.assertEqual(self.temp.valid_password("abcdefg1"), False)
    
    def test_more_than_8_characters_no_numbers(self):
        self.assertEqual(self.temp.valid_password("xyzuvwpqr@"), False)
    
    def test_more_than_8_characters_no_special(self):
        self.assertEqual(self.temp.valid_password("ijewbijvbijewv1"), False)
    
    def test_more_than_8_characters_no_upper(self):
        def.assertEqual(self.temp.valid_password("wwjieiwnecjnewjcn1#"), False)