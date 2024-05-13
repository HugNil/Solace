import customtkinter as ctk
import tkinter as tk
from PIL import Image
import pygame
from props import Props


class Settings:
    """
    Settings page of the application.
    """
    def __init__(self, app, props, return_to_gui):
        self.props = props
        self.return_to_gui = return_to_gui

        self.app = app


    def stop(self):
        """
        Stops the menu music
        """
        pygame.mixer.music.stop()
  

    def play(self):
        """
        Plays the menu music
        """
        pygame.mixer.music.load("assests/Menu music1.mp3")
        pygame.mixer.music.play(loops=1)

        pygame.mixer.music.set_volume(0.009)

    def switcher(self):
        
        if self.switch_var.get() == "on":
            self.play()
        else:
            self.stop()

    def create_frames(self):
        self.settings_window = ctk.CTkToplevel(self.app)
        self.settings_window .title("Settings")
        self.settings_frame = ctk.CTkFrame(
            master=self.settings_window,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2
            )
        self.settings_frame.configure(width=int(self.props.WIDTH * 0.8),
                                      height=int(self.props.HEIGHT * 0.5))

    def open_settings(self):
        self.create_frames()
        self.settings_window.resizable(False, False)
        self.settings_frame.pack(fill=tk.BOTH,
                                 expand=True)