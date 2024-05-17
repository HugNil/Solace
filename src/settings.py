import customtkinter as ctk
import tkinter as tk
from PIL import Image
import pygame
from src.props import Props


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
        Stops the menu music.
        """
        pygame.mixer.music.stop()
  
    def play(self):
        """
        Plays the menu music.
        """
        pygame.mixer.music.load("assests/Menu music1.mp3")
        pygame.mixer.music.play(loops=1)

        pygame.mixer.music.set_volume(0.1)

    def switcher(self):

        """
        Mutes and turns on music.
        """
        
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
        
        window_width = int(self.props.WIDTH * 0.8)
        window_height = int(self.props.HEIGHT * 0.5)
        self.settings_window.geometry(f"{window_width}x{window_height}")
        
        """
        On and off switch.
        """
        self.switch_var = ctk.StringVar(value="on")
        self.mute_switch = ctk.CTkSwitch(
            self.settings_frame,
            text="On/Off",
            variable=self.switch_var,
            onvalue="on",
            offvalue="off"
        )
        self.mute_switch.pack(pady=100,
                              padx=20)
        self.mute_switch.bind('<Button-1>', lambda e: self.switcher())


        """
        Settings window title.
        """
        self.feature_title = ctk.CTkLabel(
            master=self.settings_window,
            text='Music volume',
            font=('Arial', int(self.props.HEIGHT * 0.05), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK,
            justify='left'
        )
        self.feature_title.place(relx=0.5, rely=0.15, anchor='center')
        

    def open_settings(self):
        self.create_frames()
        self.settings_window.resizable(False, False)
        self.settings_frame.pack(fill=tk.BOTH,
                                 expand=True)