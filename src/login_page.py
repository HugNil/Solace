"""
The first page of the application, where the user can login or register.
"""

import customtkinter as ctk
import tkinter as tk
from PIL import Image
from src.log_writer import Log_writer
import json
from cryptography.fernet import Fernet
import os
import configparser
from src.collapsible_menu import CollapsibleMenu


class LoginPage:
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

        current_dir = os.getcwd()
        self.parent_dir = os.path.abspath(os.path.join(current_dir,
                                                       "../../Solace"))

        self.password_visible = False
        self.option_visible = False
        self.remember_var = tk.IntVar()
        self.logger = Log_writer()
        self.config = configparser.ConfigParser()
        self.config.read(self.open_file_with_check(self.parent_dir,
                                                   'properties.ini',
                                                   'properties.ini'))

        self.create_frames()
        self.open_images()

    def open_file_with_check(self, parent_dir, relative_path, fallback_path):
        file_path = os.path.join(parent_dir, relative_path)
        if os.path.exists(file_path):
            return file_path
        else:
            return fallback_path

    def create_frames(self):
        """
        Create all the frames for the login page.
        """
        self.start_frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2
            )
        self.start_frame.configure(width=self.props.WIDTH,
                                   height=self.props.HEIGHT)

        self.image_frame = ctk.CTkFrame(
            master=self.start_frame,
            fg_color=self.props.BACKGROUND_DARK,
            width=int(self.props.WIDTH * 0.993),
            height=int(self.props.HEIGHT * 0.95),
            corner_radius=50
        )

        self.login_frame = ctk.CTkFrame(
            master=self.start_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=int(self.props.WIDTH * 0.7),
            height=int(self.props.HEIGHT * 0.4))

        self.collapsible_menu = CollapsibleMenu(
            self.props,
            self.return_to_gui,
            self.user,
            self.start_frame
        )

        self.frames = [self.start_frame,
                       self.login_frame,
                       self.image_frame
                       ]

    def open_images(self):
        """
        Open images
        """
        self.logo_icon_img = Image.open(
            self.open_file_with_check(self.parent_dir,
                                      'assests/solace-window-icon.ico',
                                      'assests/solace-window-icon.ico'))
        self.logo_icon = ctk.CTkImage(self.logo_icon_img,
                                      size=(int(self.props.WIDTH * 0.08),
                                            int(self.props.HEIGHT * 0.05)))

        self.logo_full_img = Image.open(
            self.open_file_with_check(self.parent_dir,
                                      'assests/solace-logo-transparent.png',
                                      'assests/solace-logo-transparent.png'))
        self.logo_full = ctk.CTkImage(self.logo_full_img,
                                      size=(int(self.props.WIDTH * 0.77),
                                            int(self.props.HEIGHT * 0.19)))

        self.password_icon_img = Image.open(
            self.open_file_with_check(self.parent_dir,
                                      'assests/password-icon.png',
                                      'assests/password-icon.png'))
        self.password_icon = ctk.CTkImage(
            self.password_icon_img,
            size=(int(self.props.WIDTH * 0.06),
                  int(self.props.HEIGHT * 0.042)))

        self.email_icon_img = Image.open(
            self.open_file_with_check(self.parent_dir,
                                      'assests/username-icon.png',
                                      'assests/username-icon.png'))
        self.email_icon = ctk.CTkImage(self.email_icon_img,
                                       size=(int(self.props.WIDTH * 0.06),
                                             int(self.props.HEIGHT * 0.042)))

        self.copyright_img = Image.open(
            self.open_file_with_check(self.parent_dir,
                                      'assests/Copyright.png',
                                      'assests/Copyright.png'))
        self.copyright = ctk.CTkImage(self.copyright_img,
                                      size=(int(self.props.WIDTH * 0.83),
                                            int(self.props.HEIGHT * 0.14)))

        self.line_img = Image.open(
            self.open_file_with_check(self.parent_dir,
                                      'assests/line-without-sides.png',
                                      'assests/line-without-sides.png'))
        self.line_img = ctk.CTkImage(self.line_img,
                                     size=(int(self.props.WIDTH * 1.05),
                                           int(self.props.HEIGHT * 0.08)))

        self.show_image = ctk.CTkImage(
            Image.open(self.open_file_with_check(self.parent_dir,
                                                 'assests/show-password.png',
                                                 'assests/show-password.png')),
            size=(int(self.props.HEIGHT * 0.03),
                  int(self.props.HEIGHT * 0.035))
                  )
        
        self.hide_image = ctk.CTkImage(
            Image.open(self.open_file_with_check(self.parent_dir,
                                                 'assests/hide-password.png',
                                                 'assests/hide-password.png')),
            size=(int(self.props.HEIGHT * 0.03),
                  int(self.props.HEIGHT * 0.035))
        )

    def clear_frame(self):
        """
        Clear all the frames in the application.
        """
        for frame in self.frames:
            frame.pack_forget()
        self.logger.log('Frames cleared in home page.')

    def first_menu(self):
        """
        Create the first menu of the application.

        This is the first thing the user sees when they open the application.
        It is the login screen. The user is prompted to login or register.
        """
        self.add_collapsible_menu()
        self.collapsible_menu.lower()
        if not self.user.remember_login_var:
            # Resets the user values if not remember me was checked
            self.user.logout()
        # Makes sure the option window is closed
        self.option_visible = True

        # Opens the new first_menu
        self.start_frame.pack(fill=tk.BOTH,
                              expand=True)

        self.login_frame.place(relx=0.5,
                               rely=0.5,
                               anchor='center')

        self.image_frame.place(relx=0.5,
                               rely=0.5,
                               anchor='center')

        # Full logo
        self.logo_full_img_label = ctk.CTkLabel(master=self.start_frame,
                                                image=self.logo_full,
                                                text='')
        self.logo_full_img_label.place(relx=0.5,
                                       rely=0.175,
                                       anchor='center')
        self.create_copyright_text()
        self.create_login_form()
        self.check_remember_login()

        if os.path.exists('credentials.json'):
            email, password = self.load_login()
            self.email_entry.insert(0, email)
            self.password_entry.insert(0, password)

    def create_copyright_text(self):
        # Copyright text
        self.copyright_img = ctk.CTkLabel(master=self.start_frame,
                                          image=self.copyright,
                                          text="")
        self.copyright_img.place(relx=0.43,
                                 rely=0.92,
                                 anchor="center")

        self.line = ctk.CTkLabel(master=self.image_frame,
                                 image=self.line_img,
                                 text="")
        self.line.place(relx=0.5,
                        rely=0.8,
                        anchor="center")

    def create_login_form(self):
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
            command=lambda: self.register_user(
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

    def check_remember_login(self):
        """
        Checks in the properties.ini file if the user checked
        remember me last time they logged in. If they did, it
        checks the checkbox.
        """
        if self.config['GeneralSettings']['remember_me'] == 'True':
            self.remember_var.set(1)
        else:
            self.remember_var.set(0)

    def add_collapsible_menu(self):
        self.collapsible_menu.lower()

        open = self.open_file_with_check(self.parent_dir,
                                         'assests/menu-icon.png',
                                         'assests/menu-icon.png')
        self.collapsable_menu_img = Image.open(open)
        self.collapsable_menu_img = ctk.CTkImage(
            self.collapsable_menu_img,
            size=(int(self.props.WIDTH * 0.08),
                  int(self.props.HEIGHT * 0.05))
            )
        self.collapsable_menu_img = ctk.CTkButton(
            master=self.start_frame,
            image=self.collapsable_menu_img,
            text='',
            fg_color=self.props.BACKGROUND_DARK,
            command=lambda: self.collapsible_menu.toggle(),
            width=int(self.props.WIDTH * 0.08),
            height=int(self.props.HEIGHT * 0.05)
        )
        self.collapsable_menu_img.place(relx=0.075,
                                        rely=0.05,
                                        anchor='center')

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
        Handles the login of the user.

        This function is called when the user presses the login button.
        It checks if the user exists in the database and logs them in if
        they do. Else it shows an error message.
        """
        token = self.firebase.login_user(email, password)
        if token is not None:
            self.clear_frame()
            self.user.login(email, password, token)
            self.logger.log(f"User {email} logged in.")
            self.remember_login()
            self.return_to_gui('profile', self.user)
        else:
            self.logger.log(f"Failed login attempt for {email}.")
            self.show_sign_in_sign_up_error('login')

    def logout_handler(self) -> None:
        """
        Handle the logout of the user.
        """
        self.user.logged_in = False
        self.user.remember_login_var = False
        self.logger.log(f"User {self.user.email} logged out.")
        self.return_to_gui('home', self.user)

    def remember_login(self) -> None:
        """
        Remember the login of the user.
        """
        if self.remember_var.get() == 1:
            self.update_remember_me(True)
            self.save_login(self.user.email, self.user.password)
            self.props.remember_me = True
            print("Remembering login")
        else:
            self.update_remember_me(False)
            self.props.remember_me = False
            self.clear_credentials()
            print("Not remembering login")

    def update_remember_me(self, value) -> None:
        """
        Update the remember me value in the properties.ini file.
        """
        self.config['GeneralSettings']['remember_me'] = str(value)
        with open('properties.ini', 'w') as configfile:
            self.config.write(configfile)

    def register_user(self, email, password):
        """
        Register the user.
        """
        if email == '':
            self.show_sign_in_sign_up_error('empty_email')
        elif password == '':
            self.show_sign_in_sign_up_error('empty_password')
        else:
            status = self.firebase.register_user(email, password)
            if status == 'password_length':
                self.show_sign_in_sign_up_error('password_length')
            elif status == 'success':
                self.login_handler(email, password)

    def show_sign_in_sign_up_error(self, type):
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
        if type == 'empty_email':
            label.configure(text='Error:\nPlese enter an email.')
        elif type == 'empty_password':
            label.configure(text='Error:\nPlese enter a password.')
        elif type == 'password_length':
            label.configure(
                text='Error:\nPassword must be at least 6 characters.')
        label.place(relx=0.5, rely=0.5, anchor='center')

        popup.lift()
        popup.place(relx=0.5, rely=0.5, anchor='center')

        popup.after(3000, popup.destroy)

    def save_login(self, email, password):
        """
        Save the login of the user using encrypted password using
        fernet. Loads the key if it exists, else it generates a new key.
        """
        self.generate_key()
        key = self.load_key()
        cipher_suite = Fernet(key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        data = {
            'email': email,
            'password': encrypted_password.decode()
        }
        with open('credentials.json', 'w') as file:
            json.dump(data, file)
        self.logger.log('Login saved.')

    def load_login(self):
        """
        Load the login of the user using encrypted password using
        fernet. Loads the key if it exists, otherwise there shouldn't
        be any saved login.
        """
        key = self.load_key()
        cipher_suite = Fernet(key)
        with open('credentials.json', 'r') as file:
            data = json.load(file)
            decrypted_password = cipher_suite.decrypt(
                data['password'].encode()).decode()
            return data['email'], decrypted_password

    def generate_key(self):
        """
        Generate a key for the encryption.
        """
        if not os.path.exists('secret.key'):
            key = Fernet.generate_key()
            with open('secret.key', 'wb') as key_file:
                key_file.write(key)
            self.logger.log('Key generated.')
        else:
            self.logger.log('Key already exists.')

    def load_key(self):
        """
        Load the key for the encryption.
        """
        with open('secret.key', 'rb') as key_file:
            key = key_file.read()
        return key

    def clear_credentials(self):
        """
        Clear the credentials of the user.
        """
        try:
            os.remove('credentials.json')
            self.logger.log('Credentials removed.')
        except FileNotFoundError:
            self.logger.log('No credentials to remove.')
