"""
This module contains the Props class which is responsible for the
properties of the application.
"""


class Props:
    """
    Props class which is responsible for the properties of the application.
    """
    def __init__(self, app):
        self.app = app
        self.default_values()

    def default_values(self):
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        self.WIDTH = int(screen_width * 0.21)
        self.HEIGHT = int(screen_height * 0.6)
        self.BACKGROUND_DARK = '#014F86'
        self.BACKGROUND_LIGHT = '#89C2D9'
        self.BUTTON_COLOR = '#A9D6E5'
        self.APP_NAME = 'Solace'
        self.GRADIENT = "NightTrain.json"
        self.THEME = 'dark'
