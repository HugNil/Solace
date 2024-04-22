"""Profile page of the application"""

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from props import Props


class ProfilePage(tk.Frame):
    """Profile page of the application"""

    def __init__(self, app, return_to_gui):
        self.props = Props()
        self.return_to_gui = return_to_gui

        self.app = app

        self.create_frames()
        self.open_images()

        self.option_visible = False

    def create_frames(self):
        self.profile_frame = ctk.CTkFrame(master=self.app,
                                          fg_color=self.props.BACKGROUND_DARK,
                                          border_color=self.props.BACKGROUND_LIGHT,
                                          border_width=2)
        self.profile_frame.configure(width=self.props.WIDTH,
                                     height=self.props.HEIGHT)

        self.option_frame = ctk.CTkFrame(master=self.start_frame,
                                         fg_color=self.props.BACKGROUND_DARK,
                                         border_color=self.props.BACKGROUND_LIGHT,
                                         border_width=2,
                                         width=120,
                                         height=150)

    def open_images(self):
        self.logo_icon_img = Image.open('assests/menu logo.png')
        self.logo_icon_img.thumbnail((30, 30))
        self.logo_icon = ImageTk.PhotoImage(self.logo_icon_img)

    def profile_menu(self):
        self.profile_frame.pack(fill=tk.BOTH,
                                expand=True)

        self.logo_icon_label = ctk.CTkLabel(master=self.profile_frame,
                                            image=self.logo_icon, text='')
        self.logo_icon_label.bind('<Button-1>',
                                  lambda e: self.option_toggle())
        self.logo_icon_label.place(relx=0.075,
                                   rely=0.05,
                                   anchor='center')

    def option_toggle(self):
        if self.option_visible:
            self.option_frame.lower()
            self.option_frame.place_forget()
            self.option_visible = False
        else:
            self.option_frame.lift()
            self.option_frame.place(relx=0.075, rely=0.16, anchor='center')
            self.option_visible = True
