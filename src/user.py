"""
User class to store user information
"""


class User:
    """
    User class to store user information
    """
    def __init__(self):
        """
        Initialize the user class.
        """
        self.email = 'N/A'
        self.password = 'N/A'
        self.token = 'N/A'
        self.logged_in = False
        self.remember_login_var = False

    def reset(self):
        """
        Resets all the values of the user class to 'N/A'
        """
        self.email = 'N/A'
        self.password = 'N/A'
        self.token = 'N/A'
        self.logged_in = False
        self.remember_login_var = False

    def logout(self):
        """
        Logs out the user.
        """
        self.reset()

    def login(self, email, password, token):
        """
        Logs in the user.
        """
        self.email = email
        self.password = password
        self.token = token
        print('Logged in as'+ self.email)
