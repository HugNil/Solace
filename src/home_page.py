"""
The first page of the application, where the user can login or register.
"""

import customtkinter as ctk
import tkinter as tk
from PIL import Image


class HomePage:
    """
    The first page of the application, where the user can login or register.
    """

    def __init__(self, app, firebase, props, user, return_to_gui):
        """
        Initialize the first page of the application.
        """
        self.props = props
        self.firebase = firebase
        self.return_to_gui = return_to_gui

        self.app = app
        self.user = user

        self.password_visible = False
        self.option_visible = False
        self.remember_var = tk.IntVar()

        self.create_frames()
        self.open_images()

    def create_frames(self):
        """
        Create all the frames for the home page.
        """
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

    def open_images(self):
        """
        Open images
        """
        self.logo_icon_img = Image.open('assests/menu logo.png')
        self.logo_icon_img.thumbnail((int(self.props.WIDTH * 0.08),
                                      int(self.props.HEIGHT * 0.08)))
        self.logo_icon = ctk.CTkImage(self.logo_icon_img,
                                      size=(int(self.props.WIDTH * 0.08),
                                            int(self.props.HEIGHT * 0.05)))

        self.logo_full_img = Image.open('assests/Solace logo2 trans.png')
        self.logo_full_img.thumbnail((int(self.props.WIDTH * 0.95),
                                      int(self.props.HEIGHT * 0.95)))
        self.logo_full = ctk.CTkImage(self.logo_full_img,
                                      size=(int(self.props.WIDTH * 0.77),
                                            int(self.props.HEIGHT * 0.19)))

        self.password_icon_img = Image.open('assests/PasswordIcon.png')
        self.password_icon_img.thumbnail((int(self.props.WIDTH * 0.07),
                                          int(self.props.HEIGHT * 0.1)))
        self.password_icon = ctk.CTkImage(
            self.password_icon_img,
            size=(int(self.props.WIDTH * 0.06),
                  int(self.props.HEIGHT * 0.042)))

        self.email_icon_img = Image.open('assests/UserNameIcon.png')
        self.email_icon_img.thumbnail((int(self.props.WIDTH * 0.07),
                                       int(self.props.HEIGHT * 0.08)))
        self.email_icon = ctk.CTkImage(self.email_icon_img,
                                       size=(int(self.props.WIDTH * 0.06),
                                             int(self.props.HEIGHT * 0.042)))

        self.copyright_img = Image.open('assests/Copyright.png')
        self.copyright_img.thumbnail((int(self.props.WIDTH * 0.85),
                                      int(self.props.HEIGHT * 0.8)))
        self.copyright = ctk.CTkImage(self.copyright_img,
                                      size=(int(self.props.WIDTH * 0.83),
                                            int(self.props.HEIGHT * 0.14)))

        self.line_img = Image.open('assests/line_without_sides.png')
        self.line_img.resize((int(self.props.WIDTH),
                             int(self.props.HEIGHT)))
        self.line = ctk.CTkImage(self.line_img,
                                 size=(int(self.props.WIDTH * 0.997),
                                       int(self.props.HEIGHT * 0.08)))

    def clear_frame(self):
        """
        Clear all the frames in the application.
        """
        for frame in self.frames:
            frame.pack_forget()

    def first_menu(self):
        """
        Create the first menu of the application.
        """
        if not self.user.remember_login_var:
            # Resets the user values if not remember me was checked
            self.user.logout()
            self.show_login_frame()
        # Makes sure the option window is closed
        self.option_visible = True
        self.option_toggle()

        # Opens the new first_menu
        self.start_frame.pack(fill=tk.BOTH,
                              expand=True)

        self.login_frame.place(relx=0.5,
                               rely=0.5,
                               anchor='center')

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
        # Icon logo as option button
        self.logo_icon_label1 = ctk.CTkLabel(master=self.start_frame,
                                             image=self.logo_icon, text='')
        self.logo_icon_label1.bind("<Button-1>",
                                   command=lambda e: self.option_toggle())

        self.logo_icon_label1.place(relx=0.075,
                                    rely=0.05,
                                    anchor='center')

        # Creates alla the elements for the login frame
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
            width=int(self.props.WIDTH * 0.2),
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

        self.show_image = ctk.CTkImage(
            Image.open('assests/show.png').resize(
                (int(self.props.HEIGHT * 0.03),
                 int(self.props.HEIGHT * 0.045))),
            size=(int(self.props.HEIGHT * 0.03),
                  int(self.props.HEIGHT * 0.035))
        )
        self.hide_image = ctk.CTkImage(
            Image.open('assests/hide.png').resize(
                (int(self.props.HEIGHT * 0.03),
                 int(self.props.HEIGHT * 0.045))),
            size=(int(self.props.HEIGHT * 0.03),
                  int(self.props.HEIGHT * 0.035))
        )

        self.show_password_button = ctk.CTkLabel(
            master=self.login_frame,
            image=self.hide_image,
            text=''
        )
        self.show_password_button.bind(
            '<Button-1>', lambda e: self.toggle_show_password())
        self.show_password_button.place(relx=0.83,
                                        rely=0.345)

        self.register_button = ctk.CTkButton(
            master=self.login_frame,
            text='Register',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.2),
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
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            variable=self.remember_var,
            fg_color=self.props.BACKGROUND_LIGHT,
            text_color=self.props.BACKGROUND_LIGHT,
            hover=False,
            corner_radius=25,
            border_width=2,
            border_color=self.props.BACKGROUND_LIGHT,
            width=int(self.props.WIDTH * 0.1),
            height=int(self.props.HEIGHT * 0.05)
            )

        self.password_icon_label = ctk.CTkLabel(
            master=self.login_frame,
            image=self.password_icon,
            text='')
        self.password_icon_label.place(relx=0.12,
                                       rely=0.397,
                                       anchor='center')
        self.email_icon_label = ctk.CTkLabel(
            master=self.login_frame,
            image=self.email_icon,
            text=''
            )
        self.email_icon_label.place(relx=0.12,
                                    rely=0.198,
                                    anchor='center')

        self.remember_checkbox.place(relx=0.5, rely=0.6, anchor='center')

        # Option bar
        self.home_option = ctk.CTkLabel(
            master=self.option_frame,
            text='Home',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            height=int(self.props.HEIGHT * 0.02),
            text_color=self.props.BACKGROUND_LIGHT
            )
        self.home_option.bind(
            '<Button-1>', lambda e: self.return_to_gui('home')
            )
        self.home_option.place(relx=0.5, rely=0.15, anchor='center')

        self.settings_option = ctk.CTkLabel(
            master=self.option_frame,
            text='Settings',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            height=int(self.props.HEIGHT * 0.02),
            text_color=self.props.BACKGROUND_LIGHT
            )
        self.settings_option.bind(
            '<Button-1>', lambda e: self.return_to_gui('settings')
            )
        self.settings_option.place(relx=0.5, rely=0.85, anchor='center')

        self.profile_option = ctk.CTkLabel(
            master=self.option_frame,
            text='Profile',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            height=int(self.props.HEIGHT * 0.02),
            text_color=self.props.BACKGROUND_LIGHT
            )
        self.profile_option.bind(
            '<Button-1>',
            command=lambda e: self.return_to_gui('profile'))
        self.profile_option.place(relx=0.5, rely=0.35, anchor='center')

        self.logout_option = ctk.CTkLabel(
            master=self.option_frame,
            text='Logout',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            height=int(self.props.HEIGHT * 0.02),
            text_color=self.props.BACKGROUND_LIGHT
            )
        self.logout_option.bind('<Button-1>', lambda e: self.logout_handler())
        self.logout_option.place(relx=0.5, rely=0.65, anchor='center')
        self.logged_in_toggle()

    def option_toggle(self):
        """
        Toggle the option menu on and off.
        """
        if self.option_visible:
            self.option_frame.lower()
            self.option_frame.place_forget()
            self.option_visible = False
        else:
            self.option_frame.lift()
            self.option_frame.place(relx=0.19, rely=0.23, anchor='center')
            self.option_visible = True

    def toggle_show_password(self):
        """
        Toggle the visibility of the password entry.
        """
        if self.password_visible:
            self.password_entry.configure(show='*')
            self.show_password_button.configure(image=self.hide_image)
            self.password_visible = False
        else:
            self.password_entry.configure(show='')
            self.show_password_button.configure(image=self.show_image)
            self.password_visible = True

    def login_handler(self, email, password) -> None:
        """
        Handle the login of the user.
        """
        token = self.firebase.login_user(email, password)
        if token is not None:
            self.logged_in_toggle()
            self.remember_login()
            self.clear_frame()
            self.user.login(email, password, token)
            self.return_to_gui('profile')
        else:
            self.show_sign_in_sign_up_error()

    def logout_handler(self) -> None:
        """
        Handle the logout of the user.
        """
        self.user.logged_in = False
        self.user.remember_login_var = False
        self.logged_in_toggle()
        self.return_to_gui('home')

    def remember_login(self) -> None:
        """
        Remember the login of the user.
        """
        if self.remember_var.get() == 1:
            self.user.remember_login_var = True
            self.hide_login_frame()
            print("Remembering login")

    def register_handler(self, email, password):
        """
        Handle the registration of the user.
        """
        if self.firebase.register_user(email, password):
            self.login_handler(email, password)
        else:
            self.show_sign_in_sign_up_error()

    def logged_in_toggle(self):
        if not self.user.remember_login_var:
            self.profile_option.unbind('<Button-1>')
        if not self.user.logged_in:
            self.logout_option.unbind('<Button-1>')

    def hide_login_frame(self):
        """
        Hide the login frame.
        """
        self.login_frame.lower()
        self.login_frame.place_forget()

    def show_login_frame(self):
        """
        Show the login frame.
        """
        self.login_frame.lift()
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

    def show_sign_in_sign_up_error(self):
        """
        Show the sign in sign up error.
        """
        popup = ctk.CTkFrame(
            master=self.start_frame,
            fg_color='#1D1D1D',
            border_color='red',
            border_width=2,
            width=int(self.props.WIDTH * 0.8),
            height=int(self.props.HEIGHT * 0.15))

        label = ctk.CTkLabel(
            master=popup,
            text='Error:\nEmail or password is incorrect.',
            font=('Arial', (self.props.HEIGHT * 0.02), 'bold'),
            height=2
            )
        label.place(relx=0.5, rely=0.5, anchor='center')

        popup.lift()
        popup.place(relx=0.5, rely=0.5, anchor='center')

        popup.after(3000, popup.destroy)
