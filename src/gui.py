"""
This module contains the GUI class which is responsible for the
graphical user interface of the application.
"""

import customtkinter as ctk
from firebase_connection import FirebaseConnection
import warnings
from home_page import HomePage
from profile_page import ProfilePage
from props import Props
import pygame
from customtkinter import set_appearance_mode


warnings.filterwarnings("ignore",
                        message="CTkLabel Warning:"
                        "Given image is not CTkImage*")


class GUI:
    """
    Class for the graphical user interface of the application
    """
    def __init__(self, app) -> None:
        self.app = app

        self.props = Props(self.app)
        self.app.title(self.props.APP_NAME)
        self.app.geometry(f'{self.props.WIDTH}x{self.props.HEIGHT}')
        self.app.minsize(self.props.WIDTH, self.props.HEIGHT)
        self.app.maxsize(self.props.WIDTH, self.props.HEIGHT)
        self.app.configure(bg=self.props.BACKGROUND_DARK)
        set_appearance_mode(self.props.THEME)
        self.app.iconbitmap("assests/Solace logo1_klippt.ico")

        self.firebase = FirebaseConnection()

        self.create_frames()
        self.clear_frames()
        self.home_page.first_menu()

        pygame.mixer.init()
        self.play()

    def create_frames(self) -> None:
        """
        Creates all the frames for the application
        """
        self.home_page = HomePage(self.app, self.firebase, self.props, self.return_to_gui)
        self.profile_page = ProfilePage(self.app, self.props, self.return_to_gui)

        self.frames = [self.home_page, self.profile_page]

    def switch_frame(self, frame):
        """
        Switches the frame to the given frame
        """
        if frame == 'profile':
            self.clear_frames()
            self.profile_page.profile_menu()
        if frame == 'home':
            self.clear_frames()
            self.home_page.first_menu()

    def clear_frames(self) -> None:
        """
        Clears all the frames
        """
        for frame in self.frames:
            frame.clear_frame()

    def play(self):
        """
        Plays the menu music
        """
        pygame.mixer.music.load("assests/Menu music1.mp3")
        pygame.mixer.music.play(loops=1)

        pygame.mixer.music.set_volume(0.009)

    def stop(self):
        """
        Stops the menu music
        """
        pygame.mixer.music.stop()

    def return_to_gui(self, frame):
        """
        Returns to the gui
        """
        self.switch_frame(frame)


app = ctk.CTk()
gui = GUI(app)
pygame.mixer.init()
app.mainloop()
