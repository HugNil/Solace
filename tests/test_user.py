import unittest
from user import User  # type: ignore


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_init(self):
        self.assertEqual(self.user.email, 'N/A')
        self.assertEqual(self.user.password, 'N/A')
        self.assertEqual(self.user.token, 'N/A')
        self.assertFalse(self.user.logged_in)
        self.assertFalse(self.user.remember_login_var)

    def test_reset(self):
        self.user.email = 'test'
        self.user.password = 'test'
        self.user.token = 'test'
        self.user.logged_in = True
        self.user.remember_login_var = True
        self.user.reset()
        self.assertEqual(self.user.email, 'N/A')
        self.assertEqual(self.user.password, 'N/A')
        self.assertEqual(self.user.token, 'N/A')
        self.assertFalse(self.user.logged_in)
        self.assertFalse(self.user.remember_login_var)

    def test_logout(self):
        self.user.email = 'test'
        self.user.password = 'test'
        self.user.token = 'test'
        self.user.logged_in = True
        self.user.remember_login_var = True
        self.user.logout()
        self.assertEqual(self.user.email, 'N/A')
        self.assertEqual(self.user.password, 'N/A')
        self.assertEqual(self.user.token, 'N/A')
        self.assertFalse(self.user.logged_in)
        self.assertFalse(self.user.remember_login_var)

    def test_login(self):
        self.user.login('test', 'test', 'test')
        self.assertEqual(self.user.email, 'test')
        self.assertEqual(self.user.password, 'test')
        self.assertEqual(self.user.token, 'test')
        self.assertTrue(self.user.logged_in)


if __name__ == '__main__':
    unittest.main()
