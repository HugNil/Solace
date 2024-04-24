import customtkinter as ctk
import tkinter as tk
from PIL import Image


class Settings():
    
    def __init__(self, app, props, return_to_gui):
        self.props = props
        self.return_to_gui = return_to_gui

        self.app = app

        #Toplevel window that be over the app home- and profile page
        self.settings_window = ctk.CTkToplevel(self.app)
        self.settings_window .title("Settings")

    
    def create_frames(self):
        self.settings_frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2
            )
        self.settings_frame.configure(width=self.props.WIDTH,
                                     height=self.props.HEIGHT)
        
    def open_settings(self):
        settings_window = Settings(self.app, self.props, self.return_to_gui)
        settings_window.create_frames()
  


    