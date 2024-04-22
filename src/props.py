

class Props:
    def __init__(self, app):
        screen_width = app.winfo_screenwidth()
        screen_height = app.winfo_screenheight()
        self.WIDTH, self.HEIGHT = int(screen_width * 0.21), int(screen_height * 0.6)
        self.BACKGROUND_DARK = '#014F86'
        self.BACKGROUND_LIGHT = '#89C2D9'
        self.BUTTON_COLOR = '#A9D6E5'
        self.APP_NAME = 'Solace'
        self.GRADIENT = "NightTrain.json"
        self.THEME = 'dark'