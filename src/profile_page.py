"""Profile page of the application"""

import customtkinter as ctk
import tkinter as tk
from PIL import Image
from time import strftime


class ProfilePage():
    """Profile page of the application"""

    def __init__(self, app, props, return_to_gui):
        self.props = props
        self.return_to_gui = return_to_gui

        self.app = app

        self.create_frames()
        self.open_images()

        self.option_visible = False

    def create_frames(self):
        self.profile_frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2
            )
        self.profile_frame.configure(width=self.props.WIDTH,
                                     height=self.props.HEIGHT)

        self.option_frame = ctk.CTkFrame(master=self.profile_frame,
                                         fg_color=self.props.BACKGROUND_DARK,
                                         border_color=self.props.BACKGROUND_LIGHT,
                                         border_width=2,
                                         width=int(self.props.WIDTH * 0.3),
                                         height=int(self.props.HEIGHT * 0.3))

        self.frames = [self.option_frame, self.profile_frame]

    def open_images(self):
        self.logo_icon_img = Image.open('assests/menu logo.png')
        self.logo_icon_img.thumbnail((
            int(self.props.WIDTH * 0.08),
            int(self.props.HEIGHT * 0.08)
            ))
        self.logo_icon = ctk.CTkImage(self.logo_icon_img,
                                      size=(int(self.props.WIDTH * 0.08),
                                            int(self.props.HEIGHT * 0.05)))

    def profile_menu(self):
        self.profile_frame.pack(fill=tk.BOTH,
                                expand=True)
        self.option_visible = True
        self.option_toggle()

        self.logo_icon_label = ctk.CTkLabel(master=self.profile_frame,
                                            image=self.logo_icon, text='')
        self.logo_icon_label.bind('<Button-1>',
                                  lambda e: self.option_toggle())
        self.logo_icon_label.place(relx=0.075,
                                   rely=0.05,
                                   anchor='center')

        self.mood_button = ctk.CTkButton(
            master=self.profile_frame,
            text='Mood Form',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.2),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.return_to_gui('mood'))
        self.mood_button.place(relx=0.3,
                               rely=0.75,
                               anchor='center')

        self.excercise_button = ctk.CTkButton(
            master=self.profile_frame,
            text='  Excercises ',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.2),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.return_to_gui('excersice'))
        self.excercise_button.place(relx=0.7,
                                    rely=0.75,
                                    anchor='center')

        self.motivation_button = ctk.CTkButton(
            master=self.profile_frame,
            text=' Motivation  ',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.2),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.return_to_gui('motivation'))
        self.motivation_button.place(relx=0.3,
                                     rely=0.85,
                                     anchor='center')

        self.random_button = ctk.CTkButton(
            master=self.profile_frame,
            text='   Random    ',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.2),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.return_to_gui('random'))
        self.random_button.place(relx=0.7,
                                 rely=0.85,
                                 anchor='center')

        self.date = ctk.CTkLabel(master=self.profile_frame,
                                 text=strftime("%d %b %Y"),
                                 font=('Arial', int(self.props.HEIGHT * 0.05), 'bold'))
        self.date.place(relx=0.5,
                        rely=0.15,
                        anchor='center')

        self.time_widget = ctk.CTkLabel(master=self.profile_frame,
                                        text='',
                                        font=('Arial', int(self.props.HEIGHT * 0.05), 'bold'))
        self.time_widget.place(relx=0.5,
                               rely=0.23,
                               anchor='center')
        self.time()

        # Option bar
        self.home_option = ctk.CTkLabel(master=self.option_frame,
                                        text='Home',
                                        font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
                                        height=int(self.props.HEIGHT * 0.02),
                                        text_color=self.props.BACKGROUND_LIGHT)
        self.home_option.bind('<Button-1>', lambda e: self.return_to_gui('home'))
        self.home_option.place(relx=0.5, rely=0.15, anchor='center')

        self.settings_option = ctk.CTkLabel(master=self.option_frame,
                                            text='Settings',
                                            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
                                            height=int(self.props.HEIGHT * 0.02),
                                            text_color=self.props.BACKGROUND_LIGHT)
        self.settings_option.bind('<Button-1>', lambda e: self.return_to_gui('settings'))
        self.settings_option.place(relx=0.5, rely=0.85, anchor='center')

        self.profile_option = ctk.CTkLabel(master=self.option_frame,
                                           text='Profile',
                                           font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
                                           height=int(self.props.HEIGHT * 0.02),
                                           text_color=self.props.BACKGROUND_LIGHT)
        self.profile_option.bind('<Button-1>', lambda e: self.return_to_gui('profile'))
        self.profile_option.place(relx=0.5, rely=0.35, anchor='center')

    def option_toggle(self):
        if self.option_visible:
            self.option_frame.lower()
            self.option_frame.place_forget()
            self.option_visible = False
        else:
            self.option_frame.lift()
            self.option_frame.place(relx=0.19, rely=0.23, anchor='center')
            self.option_visible = True

    def clear_frame(self):
        """Clear all the frames in the application."""
        for frame in self.frames:
            frame.pack_forget()

    def time(self):
        time_string = strftime("%H:%M")
        self.time_widget.configure(text=time_string)
        self.time_widget.after(1000, self.time)
