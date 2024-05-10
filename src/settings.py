import customtkinter as ctk
import tkinter as tk
from PIL import Image
import pygame


class Settings():
    
    def __init__(self, app, props, return_to_gui):
        
        self.props = props
        self.return_to_gui = return_to_gui
        self.app = app
        self.settings_frame = None
        self.app.iconbitmap("assests/Solace logo1_klippt.ico")

    
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
        

    def create_frames(self):
        self.settings_frame = ctk.CTkFrame(
            master=self.app,
            bg=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=500,
            height=800)
        
                                          
    def open_settings(self):
        settings_window = ctk.CTkToplevel(self.app)
        settings_window .title("Settings")
        settings_window.resizable(False, False)
        settings_window = Settings(self.app, self.props, self.return_to_gui)
        settings_window.create_frames()
        
    
