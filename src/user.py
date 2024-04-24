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

    def reset(self):
        """
        Resets all the values of the user class to 'N/A'
        """
        self.email = 'N/A'
        self.password = 'N/A'
        self.token = 'N/A'
