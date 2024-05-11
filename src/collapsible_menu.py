import customtkinter as ctk
# import tkinter as tk
# from PIL import Image
# from time import strftime
import log_writer


class CollapsibleMenu:
    def __init__(self, props, return_to_gui, user, master_frame) -> None:
        self.props = props
        self.return_to_gui = return_to_gui
        self.user = user
        self.logger = log_writer.Log_writer()
        self.menu = ctk.CTkFrame(
            master=master_frame,
            fg_color=self.props.BACKGROUND_DARK,
            width=int(self.props.WIDTH * 0.3),
            height=int(self.props.HEIGHT * 0.3),
            border_width=2,
            border_color=self.props.BACKGROUND_LIGHT
        )
        self.is_visible = False

        self.menu.place(
            relx=0.19,
            rely=0.23,
            anchor='center')

        self.add_buttons()

    def add_buttons(self):
        self.home_button = ctk.CTkButton(
            master=self.menu,
            text='Home',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            fg_color=self.props.BACKGROUND_DARK,
            text_color=self.props.BACKGROUND_LIGHT,
            width=10,
            height=16,
            hover_color="#033253",
            corner_radius=8,
            command=lambda: self.switch_frame('Home', self.user)
        )
        self.home_button.pack(pady=(10, 5), padx=10)

        self.profile_button = ctk.CTkButton(
            master=self.menu,
            text='Profile',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            fg_color=self.props.BACKGROUND_DARK,
            text_color=self.props.BACKGROUND_LIGHT,
            width=10,
            height=16,
            border_color=self.props.BACKGROUND_LIGHT,
            hover_color="#033253",
            command=None,
            corner_radius=8
        )
        self.profile_button.pack(pady=5, padx=10)

        self.settings_button = ctk.CTkButton(
            master=self.menu,
            text='Settings',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            fg_color=self.props.BACKGROUND_DARK,
            text_color=self.props.BACKGROUND_LIGHT,
            width=10,
            height=16,
            hover_color="#033253",
            corner_radius=8,
            command=lambda: self.switch_frame('settings', self.user)
        )
        self.settings_button.pack(pady=(40, 5), padx=10)

        self.logout_button = ctk.CTkButton(
            master=self.menu,
            text='Logout',
            font=('Arial', int(self.props.HEIGHT * 0.025), 'bold'),
            fg_color=self.props.BACKGROUND_DARK,
            text_color=self.props.BACKGROUND_LIGHT,
            width=10,
            height=16,
            hover_color="#033253",
            corner_radius=8,
            command=lambda: self.logout(self.user, self.return_to_gui)
        )
        self.logout_button.pack(pady=(5, 10), padx=10)

    def switch_frame(self, frame, user):
        self.return_to_gui(frame, user)

    def logout(self, user, return_to_gui):
        self.logger.log(f'User {user.email} logged out.')
        print(f'User {user.email} logged out.')
        user.logout()
        return_to_gui('home', user)

    def toggle(self):
        if self.is_visible:
            self.menu.lower()
        else:
            self.menu.lift()
        self.is_visible = not self.is_visible

    def lift(self):
        self.menu.lift()

    def lower(self):
        self.menu.lower()
