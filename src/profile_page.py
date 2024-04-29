"""
Profile page of the application
"""

import customtkinter as ctk
import tkinter as tk
from PIL import Image
from time import strftime
import log_writer
import collapsible_menu


class ProfilePage():
    """
    Profile page of the application
    """

    def __init__(self, app, props, user, return_to_gui):
        """
        Initialize the first page of the application.
        """
        self.props = props
        self.return_to_gui = return_to_gui
        self.user = user
        self.logger = log_writer.Log_writer()
        self.logger.log('Profile page opened.')
        self.collapsible_menu_visible = False
        self.option_visible = False
        self.app = app

        self.dashboardPage()

        self.frames = [
            self.profile_frame,
            self.option_frame,
            self.button_frame,
            self.image_frame
            ]

    def initialize(self):
        """
        Initialize the profile page.
        """
        self.create_frames()
        self.open_images()

        self.collapsible_menu = collapsible_menu.CollapsibleMenu(
            self.props,
            self.return_to_gui,
            self.user,
            self.profile_frame
        )

    def create_frames(self):
        """
        Creates all the frames for the application.
        """
        self.profile_frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2
            )
        self.profile_frame.configure(width=self.props.WIDTH,
                                     height=self.props.HEIGHT)

        self.option_frame = ctk.CTkFrame(
            master=self.profile_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=int(self.props.WIDTH * 0.3),
            height=int(self.props.HEIGHT * 0.3)
            )

    def open_images(self):
        """
        Opens all the images for the page.
        """
        self.logo_icon_img = Image.open('assests/menu-icon.png')
        self.logo_icon = ctk.CTkImage(self.logo_icon_img,
                                      size=(int(self.props.WIDTH * 0.08),
                                            int(self.props.HEIGHT * 0.05)))

    # def profile_menu(self):
    #     """
    #     Profile menu of the profile page.
    #     """
    #     self.profile_frame.pack(fill=tk.BOTH,
    #                             expand=True)
    #     self.option_visible = True
    #     self.option_toggle()

    #     self.logo_icon_label = ctk.CTkLabel(master=self.profile_frame,
    #                                         image=self.logo_icon, text='')
    #     self.logo_icon_label.bind('<Button-1>',
    #                               lambda e: self.option_toggle())
    #     self.logo_icon_label.place(relx=0.075,
    #                                rely=0.05,
    #                                anchor='center')

    #     self.mood_button = ctk.CTkButton(
    #         master=self.profile_frame,
    #         text='Mood Form',
    #         font=('Arial', int(self.props.HEIGHT * 0.02)),
    #         width=int(self.props.WIDTH * 0.2),
    #         corner_radius=32,
    #         fg_color=self.props.BUTTON_COLOR,
    #         text_color='black',
    #         border_color=self.props.BACKGROUND_LIGHT,
    #         border_width=2,
    #         hover_color='white',
    #         command=lambda: self.return_to_gui('mood'))
    #     self.mood_button.place(relx=0.3,
    #                            rely=0.75,
    #                            anchor='center')

    #     self.excercise_button = ctk.CTkButton(
    #         master=self.profile_frame,
    #         text='  Excercises ',
    #         font=('Arial', int(self.props.HEIGHT * 0.02)),
    #         width=int(self.props.WIDTH * 0.2),
    #         corner_radius=32,
    #         fg_color=self.props.BUTTON_COLOR,
    #         text_color='black',
    #         border_color=self.props.BACKGROUND_LIGHT,
    #         border_width=2,
    #         hover_color='white',
    #         command=lambda: self.return_to_gui('excersice'))
    #     self.excercise_button.place(relx=0.7,
    #                                 rely=0.75,
    #                                 anchor='center')

    #     self.motivation_button = ctk.CTkButton(
    #         master=self.profile_frame,
    #         text=' Motivation  ',
    #         font=('Arial', int(self.props.HEIGHT * 0.02)),
    #         width=int(self.props.WIDTH * 0.2),
    #         corner_radius=32,
    #         fg_color=self.props.BUTTON_COLOR,
    #         text_color='black',
    #         border_color=self.props.BACKGROUND_LIGHT,
    #         border_width=2,
    #         hover_color='white',
    #         command=lambda: self.return_to_gui('motivation'))
    #     self.motivation_button.place(relx=0.3,
    #                                  rely=0.85,
    #                                  anchor='center')

    #     self.random_button = ctk.CTkButton(
    #         master=self.profile_frame,
    #         text='   Random    ',
    #         font=('Arial', int(self.props.HEIGHT * 0.02)),
    #         width=int(self.props.WIDTH * 0.2),
    #         corner_radius=32,
    #         fg_color=self.props.BUTTON_COLOR,
    #         text_color='black',
    #         border_color=self.props.BACKGROUND_LIGHT,
    #         border_width=2,
    #         hover_color='white',
    #         command=lambda: self.return_to_gui('random'))
    #     self.random_button.place(relx=0.7,
    #                              rely=0.85,
    #                              anchor='center')

    #     self.date = ctk.CTkLabel(
    #         master=self.profile_frame,
    #         text=strftime("%d %b %Y"),
    #         font=('Arial', int(self.props.HEIGHT * 0.05), 'bold')
    #         )
    #     self.date.place(relx=0.5,
    #                     rely=0.15,
    #                     anchor='center')

    #     self.time_widget = ctk.CTkLabel(
    #         master=self.profile_frame,
    #         text='',
    #         font=('Arial', int(self.props.HEIGHT * 0.05), 'bold'))
    #     self.time_widget.place(relx=0.5,
    #                            rely=0.23,
    #                            anchor='center')
    #     self.time()

    #     # Option bar
    #     self.home_option = ctk.CTkLabel(
    #         master=self.option_frame,
    #         text='Home',
    #         font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
    #         height=int(self.props.HEIGHT * 0.02),
    #         text_color=self.props.BACKGROUND_LIGHT
    #         )
    #     self.home_option.bind(
    #         '<Button-1>', lambda e: self.return_to_gui('home')
    #         )
    #     self.home_option.place(relx=0.5, rely=0.15, anchor='center')

    #     self.settings_option = ctk.CTkLabel(
    #         master=self.option_frame,
    #         text='Settings',
    #         font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
    #         height=int(self.props.HEIGHT * 0.02),
    #         text_color=self.props.BACKGROUND_LIGHT
    #         )
    #     self.settings_option.bind(
    #         '<Button-1>', lambda e: self.return_to_gui('settings')
    #         )
    #     self.settings_option.place(relx=0.5, rely=0.85, anchor='center')

    #     self.profile_option = ctk.CTkLabel(
    #         master=self.option_frame,
    #         text='Profile',
    #         font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
    #         height=int(self.props.HEIGHT * 0.02),
    #         text_color=self.props.BACKGROUND_LIGHT
    #         )
    #     self.profile_option.bind(
    #         '<Button-1>', lambda e: self.return_to_gui('profile')
    #         )
    #     self.profile_option.place(relx=0.5, rely=0.35, anchor='center')

    #     self.logout_option = ctk.CTkLabel(
    #         master=self.option_frame,
    #         text='Logout',
    #         font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
    #         height=int(self.props.HEIGHT * 0.02),
    #         text_color=self.props.BACKGROUND_LIGHT
    #         )
    #     self.logout_option.bind('<Button-1>',
    # lambda e: self.logout_handler())
    #     self.logout_option.place(relx=0.5, rely=0.65, anchor='center')

    def dashboardPage(self):
        """
        Dashboard page of the profile page.
        """
        self.initialize()
        self.logger.log('Initializing dashboard page.')
        self.add_images()

        self.profile_frame.pack(fill=tk.BOTH,
                                expand=True)
        self.date = ctk.CTkLabel(
            master=self.profile_frame,
            text=strftime("%d %b %Y"),
            font=('Arial', int(self.props.HEIGHT * 0.05), 'bold')
            )
        self.date.pack(pady=(50, 10))

        self.time_widget = ctk.CTkLabel(
            master=self.profile_frame,
            text=strftime("%H:%M"),
            font=('Arial', int(self.props.HEIGHT * 0.05), 'bold'))
        self.time_widget.pack()

        self.create_buttons_grid()
        # self.collapsible_menu.add(self.profile_frame)
        # self.add_collapsible_menu()

    def create_buttons_grid(self):
        """
        Creates the buttons grid for the dashboard page.
        """
        self.button_frame = ctk.CTkFrame(
            master=self.profile_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=0
            )
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        self.mood_button = ctk.CTkButton(
            master=self.button_frame,
            text='Register Mood',
            font=('Arial', int(self.props.HEIGHT * 0.02), 'bold'),
            height=int(self.props.HEIGHT * 0.1),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=self.open_mood_form)
        self.mood_button.grid(row=0, column=0, padx=10, pady=10)

        self.exercises_button = ctk.CTkButton(
            master=self.button_frame,
            text='Exercises',
            font=('Arial', int(self.props.HEIGHT * 0.02), 'bold'),
            height=int(self.props.HEIGHT * 0.1),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.return_to_gui('exercise'))
        self.exercises_button.grid(row=0, column=1, padx=10, pady=10)

        self.motivation_button = ctk.CTkButton(
            master=self.button_frame,
            text='Motivation',
            font=('Arial', int(self.props.HEIGHT * 0.02), 'bold'),
            height=int(self.props.HEIGHT * 0.1),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.return_to_gui('motivation'))
        self.motivation_button.grid(row=1, column=0, padx=10, pady=10)

        self.summary_button = ctk.CTkButton(
            master=self.button_frame,
            text='Summary',
            font=('Arial', int(self.props.HEIGHT * 0.02), 'bold'),
            height=int(self.props.HEIGHT * 0.1),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.return_to_gui('summary'))
        self.summary_button.grid(row=1, column=1, padx=10, pady=10)

        self.button_frame.pack(pady=(150, 0))

    def add_images(self):
        """
        Creates a frame for the images and adds the images.
        """
        self.image_frame = ctk.CTkFrame(
            master=self.profile_frame,
            fg_color=self.props.BACKGROUND_DARK,
            width=int(self.props.WIDTH * 0.993),
            height=int(self.props.HEIGHT * 0.95),
            corner_radius=50
        )
        self.image_frame.place(relx=0.5,
                               rely=0.5,
                               anchor='center')

        self.line = Image.open('assests/line-without-sides.png')
        self.line = ctk.CTkImage(
            self.line,
            size=(int(self.props.WIDTH * 1),
                  int(self.props.HEIGHT * 0.1))
            )
        self.line = ctk.CTkLabel(
            master=self.image_frame,
            image=self.line,
            text=""
            )
        self.line.place(relx=0.5, rely=0.87, anchor='center')

        self.collapsable_menu_img = Image.open('assests/menu-icon.png')
        self.collapsable_menu_img = ctk.CTkImage(
            self.collapsable_menu_img,
            size=(int(self.props.WIDTH * 0.08),
                  int(self.props.HEIGHT * 0.05))
            )
        self.collapsable_menu_img = ctk.CTkButton(
            master=self.profile_frame,
            image=self.collapsable_menu_img,
            text='',
            fg_color=self.props.BACKGROUND_DARK,
            command=self.collapsible_menu.toggle,
            width=int(self.props.WIDTH * 0.08),
            height=int(self.props.HEIGHT * 0.05)
        )
        self.collapsable_menu_img.place(relx=0.075,
                                        rely=0.05,
                                        anchor='center')

    # def add_collapsible_menu(self):
    #     self.collapsable_menu = ctk.CTkFrame(
    #         master=self.profile_frame,
    #         fg_color=self.props.BACKGROUND_DARK,
    #         width=int(self.props.WIDTH * 0.3),
    #         height=int(self.props.HEIGHT * 0.3),
    #         border_width=2,
    #         border_color=self.props.BACKGROUND_LIGHT
    #     )
    #     self.collapsable_menu.place(
    #         relx=0.19,
    #         rely=0.23,
    #         anchor='center')
    #     self.collapsable_menu.lower()

    # def toggle_collapsible_menu(self):
    #     if self.collapsible_menu_visible:
    #         self.collapsable_menu.lower()
    #         self.collapsible_menu_visible = False
    #     else:
    #         self.collapsable_menu.lift()
    #         self.collapsible_menu_visible = True

    # def option_toggle(self):
    #     """
    #     toggle option menu.
    #     """
    #     if self.option_visible:
    #         self.option_frame.lower()
    #         self.option_frame.place_forget()
    #         self.option_visible = False
    #         self.logger.log('Option menu closed.')
    #     else:
    #         self.option_frame.lift()
    #         self.option_frame.place(relx=0.19, rely=0.23, anchor='center')
    #         self.option_visible = True
    #         self.logger.log('Option menu opened.')

    def open_mood_form(self):
        """
        Open the mood form.
        """
        # self.change_to_mood_registration()
        # self.mood_registration = mood_registration.MoodRegistration(
        #     self.app,
        #     self.props,
        #     self.user,
        #     self.return_to_gui
        # )
        self.logger.log('Button <Register Mood> clicked.')
        self.return_to_gui('mood_registration', self.user)

    def change_to_mood_registration(self):
        self.clear_frame()

    def clear_frame(self):
        """
        Clear all the frames in the application.
        """
        self.frames = [
            self.profile_frame,
            self.option_frame,
            self.button_frame,
            self.image_frame
        ]
        for frame in self.frames:
            frame.pack_forget()

    def time(self):
        """
        Time widget.
        """
        time_string = strftime("%H:%M")
        self.time_widget.configure(text=time_string)
        self.time_widget.after(1000, self.time)

    def logout_handler(self):
        """
        Logout handler.
        """
        self.clear_frame()
        self.logger.log(f'User {self.user.email} logged out.')
        self.user.logout()
        self.return_to_gui('home')
