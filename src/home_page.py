"""The first page of the application, where the user can login or register."""

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from props import Props


class HomePage:
    """
    The first page of the application, where the user can login or register.
    """

    def __init__(self, app, firebase, return_to_gui):
        """Initialize the first page of the application."""
        self.props = Props(app)
        self.firebase = firebase
        self.return_to_gui = return_to_gui

        self.button_width = int(self.props.WIDTH * 0.2)
        self.button_height = int(self.props.HEIGHT * 0.05)

        self.app = app

        self.start_frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2
            )
        self.start_frame.configure(width=self.props.WIDTH,
                                   height=self.props.HEIGHT)

        self.option_frame = ctk.CTkFrame(
            master=self.start_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=int(self.props.WIDTH * 0.3),
            height=int(self.props.HEIGHT * 0.3)
            )

        self.login_frame = ctk.CTkFrame(
            master=self.start_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=int(self.props.WIDTH * 0.7),
            height=int(self.props.HEIGHT * 0.4))

        self.frames = [self.start_frame,
                       self.option_frame,
                       self.login_frame]

        self.password_visible = False
        self.option_visible = False
        self.remember_var = tk.IntVar()
        self.remember_email = None
        self.remember_password = None
        self.remember_token = None

        self.logo_icon_img = Image.open('assests/menu logo.png')
        self.logo_icon_img.thumbnail((int(self.props.WIDTH * 0.08),
                                      int(self.props.HEIGHT * 0.08)))
        self.logo_icon = ImageTk.PhotoImage(self.logo_icon_img)

        self.logo_full_img = Image.open('assests/Solace logo2 trans.png')
        self.logo_full_img.thumbnail((int(self.props.WIDTH * 0.95),
                                      int(self.props.HEIGHT * 0.95)))
        self.logo_full = ImageTk.PhotoImage(self.logo_full_img)

        self.foregound_img = Image.open('assests/Solace_background1.png')
        self.foregound_img.thumbnail((int(self.props.WIDTH * 1.25),
                                      int(self.props.HEIGHT * 1.25)))
        self.foreground = ImageTk.PhotoImage(self.foregound_img)

        self.password_icon_img = Image.open('assests/PasswordIcon.png')
        self.password_icon_img.thumbnail((int(self.props.WIDTH * 0.07),
                                          int(self.props.HEIGHT * 0.1)))
        self.password_icon = ImageTk.PhotoImage(self.password_icon_img)

        self.email_icon_img = Image.open('assests/UserNameIcon.png')
        self.email_icon_img.thumbnail((int(self.props.WIDTH * 0.07),
                                       int(self.props.HEIGHT * 0.1)))
        self.email_icon = ImageTk.PhotoImage(self.email_icon_img)

        self.copyright_img = Image.open('assests/Copyright.png')
        self.copyright_img.thumbnail((int(self.props.WIDTH * 0.85),
                                      int(self.props.HEIGHT * 0.85)))
        self.copyright = ImageTk.PhotoImage(self.copyright_img)

        self.line_img = Image.open('assests/line_without_sides.png')
        self.line_img.thumbnail((int(self.props.WIDTH * 0.997),
                                 int(self.props.HEIGHT)))
        self.line = ImageTk.PhotoImage(self.line_img)

    def clear_frame(self):
        """Clear all the frames in the application."""
        for frame in self.frames:
            frame.pack_forget()

    def first_menu(self):
        """Create the first menu of the application."""
        # Clear old frames

        # Opens the new first_menu
        self.start_frame.pack(fill=tk.BOTH,
                              expand=True)

        self.login_frame.place(relx=0.5,
                               rely=0.5,
                               anchor='center')

        self.foregound_img = ctk.CTkLabel(master=self.start_frame,
                                          image=self.foreground,
                                          text="")
        # self.foregound_img.place(relx=0.5,
        #                         rely=0.45,
        #                         anchor='center')

        # Full logo
        self.logo_full_img_label = ctk.CTkLabel(master=self.start_frame,
                                                image=self.logo_full,
                                                text='')
        self.logo_full_img_label.place(relx=0.5,
                                       rely=0.175,
                                       anchor='center')

        # Copyright text
        self.copyright_img = ctk.CTkLabel(master=self.start_frame,
                                          image=self.copyright,
                                          text="")

        self.copyright_img.place(relx=0.43,
                                 rely=0.92,
                                 anchor="center")

        self.line_img = ctk.CTkLabel(master=self.start_frame,
                                     image=self.line,
                                     text="")

        self.line_img.place(relx=0.497,
                            rely=0.8,
                            anchor="center")
        # Icon logo as home button
        self.logo_icon_label1 = ctk.CTkLabel(master=self.start_frame,
                                             image=self.logo_icon, text='')
        # Icon logo as mini-menu
        self.logo_icon_label1.bind("<Button-1>",
                                   command=lambda e: self.option_toggle())

        self.logo_icon_label1.place(relx=0.075,
                                    rely=0.05,
                                    anchor='center')

        # Creates alla the elements for the first frame
        self.email_label = ctk.CTkLabel(
            master=self.login_frame,
            text='Email',
            font=('Arial', int(self.props.HEIGHT * 0.02), 'bold'),
            height=int(self.props.HEIGHT * 0.02),
            text_color=self.props.BACKGROUND_LIGHT
            )

        self.email_label.place(relx=0.5,
                               rely=0.12,
                               anchor='center')
        self.email_entry = ctk.CTkEntry(
            master=self.login_frame,
            placeholder_text='Email',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.45),
            height=int(self.props.HEIGHT * 0.02),
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2
            )
        self.email_entry.place(relx=0.5,
                               rely=0.2,
                               anchor='center')

        self.login_button = ctk.CTkButton(
            master=self.login_frame,
            text='  Login  ',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=self.button_width,
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda:
            self.login_handler(
                self.email_entry.get(),
                self.password_entry.get()))
        self.login_button.place(relx=0.32,
                                rely=0.8,
                                anchor='center')

        self.password_label = ctk.CTkLabel(
            master=self.login_frame,
            text='Password',
            font=('Arial', int(self.props.HEIGHT * 0.02), 'bold'),
            height=int(self.props.HEIGHT * 0.02),
            text_color=self.props.BACKGROUND_LIGHT
            )
        self.password_label.place(relx=0.5,
                                  rely=0.32,
                                  anchor='center')
        self.password_entry = ctk.CTkEntry(
            master=self.login_frame,
            placeholder_text='Password',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.45),
            height=int(self.props.HEIGHT * 0.02),
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            show='*'
            )
        self.password_entry.place(relx=0.5,
                                  rely=0.4,
                                  anchor='center')

        self.show_image = ImageTk.PhotoImage(
            Image.open('assests/show.png').resize((int(self.props.HEIGHT * 0.035),
                                                   int(self.props.HEIGHT * 0.045))))
        self.hide_image = ImageTk.PhotoImage(
            Image.open('assests/hide.png').resize((int(self.props.HEIGHT * 0.035),
                                                   int(self.props.HEIGHT * 0.045))))

        self.show_password_button = ctk.CTkLabel(
            master=self.login_frame,
            image=self.hide_image,
            text=''
            )
        self.show_password_button.bind(
            '<Button-1>', lambda e: self.toggle_show_password())
        self.show_password_button.place(relx=0.83,
                                        rely=0.32,)

        self.register_button = ctk.CTkButton(
            master=self.login_frame,
            text='Register',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=self.button_width,
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=lambda: self.register_handler(
                self.email_entry.get(),
                self.password_entry.get()
                ))
        self.register_button.place(relx=0.68,
                                   rely=0.8,
                                   anchor='center')

        self.remember_checkbox = ctk.CTkCheckBox(
            master=self.login_frame,
            text='Remember Me',
            variable=self.remember_var,
            fg_color=self.props.BACKGROUND_LIGHT,
            text_color=self.props.BACKGROUND_LIGHT,
            hover=False,
            corner_radius=25,
            border_width=2,
            border_color=self.props.BACKGROUND_LIGHT,
            width=int(self.props.WIDTH * 0.1),
            height=int(self.props.HEIGHT * 0.1)
            )

        self.password_icon_label = ctk.CTkLabel(master=self.login_frame,
                                                image=self.password_icon,
                                                text='')
        self.password_icon_label.place(relx=0.12,
                                       rely=0.395,
                                       anchor='center')
        self.email_icon_label = ctk.CTkLabel(master=self.login_frame,
                                             image=self.email_icon,
                                             text='')
        self.email_icon_label.place(relx=0.12,
                                    rely=0.195,
                                    anchor='center')

        # self.remember_checkbox.place(relx=0.5, rely=0.54, anchor='center')

    def option_toggle(self):
        """Toggle the option menu on and off."""
        if self.option_visible:
            self.option_frame.place_forget()
            self.option_visible = False
        else:
            self.option_frame.place(relx=0.19, rely=0.23, anchor='center')
            self.option_visible = True

    def toggle_show_password(self):
        """Toggle the visibility of the password entry."""
        if self.password_visible:
            self.password_entry.configure(show='*')
            self.show_password_button.configure(image=self.hide_image)
            self.password_visible = False
        else:
            self.password_entry.configure(show='')
            self.show_password_button.configure(image=self.show_image)
            self.password_visible = True

    def login_handler(self, email, password) -> None:
        """Handle the login of the user."""
        self.token = self.firebase.login_user(email, password)
        if self.token is not None:
            self.remember_login()
            self.clear_frame()
            self.return_to_gui('profile')

    def remember_login(self) -> None:
        """Remember the login of the user."""
        if self.remember_var.get() == 1:
            self.remember_email = self.email_entry.get()
            self.remember_password = self.password_entry.get()
            self.remember_token = self.token
            print("Remembering login")

    def register_handler(self, email, password):
        """Handle the registration of the user."""
        if self.firebase.register_user(email, password):
            return 'profile'
