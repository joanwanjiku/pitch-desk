from app.models import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'foobar')

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password