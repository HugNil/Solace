import customtkinter as ctk
import log_writer


class CollapsibleMenu:
    """
    This class is responsible for creating a collapsible menu.
    """
    def __init__(self, props, return_to_gui, user, master_frame) -> None:
        """
        Initializes the CollapsibleMenu class.

        Parameters:
        props (object): UI settings like colors and dimensions.
        return_to_gui (function): Callback function to switch frames.
        user (object): The current user object.
        master_frame (tk.Frame): The parent frame for the menu.
        """
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

        self.menu.place(relx=0.19, rely=0.23, anchor='center')

        self.add_buttons()

    def add_buttons(self):
        """
        Adds buttons to the collapsible menu.
        """
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
            command=lambda: self.switch_frame('profile', self.user)
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
        """
        Switches to the specified frame.

        Parameters:
        frame (str): The name of the frame to switch to.
        user (object): The current user object.
        """
        self.return_to_gui(frame, user)

    def logout(self, user, return_to_gui):
        """
        Logs out the current user.

        Parameters:
        user (object): The current user object.
        return_to_gui (function): Callback function to return to home frame.
        """
        self.logger.log(f'User {user.email} logged out.')
        user.logout()
        return_to_gui('home', user)

    def toggle(self):
        """
        Toggles the visibility of the collapsible menu.
        """
        if self.is_visible:
            self.lower()
        else:
            self.lift()
        self.is_visible = not self.is_visible

    def lift(self):
        """
        Brings the menu to the front.
        """
        self.menu.lift()

    def lower(self):
        """
        Sends the menu to the back.
        """
        self.menu.lower()
