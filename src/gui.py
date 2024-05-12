"""
This module contains the GUI class which is responsible for the
graphical user interface of the application.
"""

import customtkinter as ctk
from firebase_connection import FirebaseConnection
from login_page import LoginPage
from profile_page import ProfilePage
from settings import Settings
from mood_registration import MoodRegistration
from summary import Summary
from props import Props
import pygame
from customtkinter import set_appearance_mode
from user import User
import log_writer
from Exercise import Exercise


class GUI:
    """
    Class for the graphical user interface of the application
    """
    def __init__(self, app) -> None:
        self.app = app

        self.logger = log_writer.Log_writer()
        self.logger.clear_log()
        self.logger.log('Application started.')

        self.user = User()
        self.props = Props(self.app)
        self.app.title(self.props.APP_NAME)
        self.app.geometry(f'{self.props.WIDTH}x{self.props.HEIGHT}')
        self.app.resizable(False, False)
        self.app.configure(bg=self.props.BACKGROUND_DARK)
        set_appearance_mode(self.props.THEME)
        self.app.iconbitmap("assests/solace-window-icon.ico")

        self.firebase = FirebaseConnection()

        self.create_frames()
        self.clear_frames()
        self.login_page.first_menu()

        pygame.mixer.init()
        self.play()

    def create_frames(self) -> None:
        """
        Creates all the frames for the application
        """
        self.login_page = LoginPage(
            self.app,
            self.firebase,
            self.props,
            self.user,
            self.return_to_gui
            )
        self.profile_page = ProfilePage(
            self.app,
            self.props,
            self.user,
            self.return_to_gui
            )
        self.settings = Settings(
            self.app,
            self.props,
            self.return_to_gui
            )
        self.mood_registration = MoodRegistration(
            self.app,
            self.props,
            self.user,
            self.return_to_gui
            )
        self.summary = Summary(
            self.app,
            self.props,
            self.user,
            self.return_to_gui
        )
        # self.exercise_page = Exercise(  # Comment out
        #     self.app,                   # if error -------
        #     self.return_to_gui,         # ----------------
        #     self.user,                  # ----------------
        #     self.props                  # ----------------
        #     )
        self.frames = [
            self.login_page,
            self.profile_page,
            self.mood_registration,
            self.summary,
            # self.exercise_page        # Comment out if error
            ]

    def switch_frame(self, frame, user):
        """
        Switches the frame to the given frame
        """
        if frame == 'profile':
            if user.logged_in:
                self.clear_frames()
                self.logger.log('Clearing frames')
                self.logger.log('Opening profile page')
                self.profile_page.dashboardPage()
            else:
                self.clear_frames()
                self.login_page.first_menu()
        if frame == 'home':
            self.clear_frames()
            self.login_page.first_menu()
        if frame == 'settings':
            self.settings.open_settings()
            print('returned from mood registration')
        if frame == 'mood_registration':
            self.clear_frames()
            self.logger.log('Clearing frames')
            self.logger.log('Opening mood registration page')
            self.mood_registration.create_widgets()
        if frame == 'summary':
            self.clear_frames()
            self.logger.log('Clearing frames')
            self.logger.log('Opening summary page')
            self.summary.create_f()
        # if frame == 'exercise':                       # Comment out
        #     self.clear_frames()                       # if error --
        #     self.logger.log('Clearing frames')        # -----------
        #     self.logger.log('Opening exercise page')  # -----------
        #     self.exercise_page.create_widgets()       # -----------

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
        pygame.mixer.music.load("assests/music-menu.mp3")
        pygame.mixer.music.play(loops=1)
        pygame.mixer.music.set_volume(0.009)
        self.logger.log('Menu music started.')

    def stop(self):
        """
        Stops the menu music
        """
        pygame.mixer.music.stop()
        self.logger.log('Menu music stopped.')

    def return_to_gui(self, frame, user):
        """
        Returns to the gui
        """
        self.switch_frame(frame, user)

    def run_app():
        """
        Runs the application
        """
        app = ctk.CTk()
        GUI(app)
        pygame.mixer.init()
        app.mainloop()


if __name__ == '__main__':
    GUI.run_app()
