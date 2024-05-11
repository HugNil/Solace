import customtkinter as ctk
from PIL import Image
import collapsible_menu
import log_writer
import firebase_connection
from graph import Graph


class Summary:
    """
    This class is responsible for the Summary.
    """
    def __init__(self, app, props, user, return_to_gui):
        self.app = app
        self.props = props
        self.user = user
        self.return_to_gui = return_to_gui
        self.logger = log_writer.Log_writer()
        self.firebase = firebase_connection.FirebaseConnection()
        self.create_f()
        self.frames = [self.main_frame]

    def create_f(self):
        """
        Creates the frames for the Summary.
        """
        self.main_frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=self.props.WIDTH,
            height=self.props.HEIGHT
        )
        self.main_frame.pack(fill='both', expand=True)

        self.create_image_frame()
        self.add_collapsible_menu()
        self.add_back_button()
        self.create_info_label()
        self.add_graph()

    def add_back_button(self):
        self.back_button_img = Image.open('assests/back-button.png')
        self.back_button_img = ctk.CTkImage(
            self.back_button_img,
            size=(int(self.props.WIDTH * 0.15),
                  int(self.props.HEIGHT * 0.0375))
        )
        self.back_button = ctk.CTkButton(
            master=self.main_frame,
            image=self.back_button_img,
            fg_color=self.props.BACKGROUND_DARK,
            command=lambda: self.return_to_gui("profile", self.user),
            text='',
            width=int(self.props.WIDTH * 0.15),
            height=int(self.props.HEIGHT * 0.0375)
        )
        self.back_button.place(relx=0.85, rely=0.05, anchor='center')

    def create_info_label(self):
        """
        Creates a bolder title of the name of this feature. It also adds
        a shorter description and guide of the feature.
        """
        self.feature_title = ctk.CTkLabel(
            master=self.main_frame,
            text='Mood Summary',
            font=('Arial', int(self.props.HEIGHT * 0.05), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK,
            justify='left'
        )
        self.feature_title.place(relx=0.35, rely=0.15, anchor='center')

        self.feature_description = ctk.CTkLabel(
            master=self.main_frame,
            text='''
Here is a summary of your mood
the past 7 days.
            ''',
            font=('Arial', int(self.props.HEIGHT * 0.0257)),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK,
            justify='left'
        )
        self.feature_description.place(relx=0.355, rely=0.245, anchor='center')

    def create_image_frame(self):
        """
        Creates a separate frame for images to not overlap the border.
        """
        self.image_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color=self.props.BACKGROUND_DARK,
            width=int(self.props.WIDTH * 0.989),
            height=int(self.props.HEIGHT * 0.95),
            corner_radius=50
        )
        self.image_frame.place(relx=0.498,
                               rely=0.5,
                               anchor='center')

        self.line = Image.open("assests/line-without-sides.png")
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

    def add_collapsible_menu(self):
        self.collapsible_menu = collapsible_menu.CollapsibleMenu(
            self.props,
            self.return_to_gui,
            self.user,
            self.main_frame
        )
        self.collapsible_menu.lower()

        self.collapsable_menu_img = Image.open('assests/menu-icon.png')
        self.collapsable_menu_img = ctk.CTkImage(
            self.collapsable_menu_img,
            size=(int(self.props.WIDTH * 0.08),
                  int(self.props.HEIGHT * 0.05))
            )
        self.collapsable_menu_img = ctk.CTkButton(
            master=self.main_frame,
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

    def add_graph(self):
        self.graph = Graph(self.image_frame, self.props)
        self.graph.display()

        x_data = [1, 2, 3, 4, 5, 6, 7]
        y_data = [1, 3, 2, 4, 7, 5, 3]

        self.graph.plot_data(x_data, y_data)

    def back(self):
        self.main_frame.destroy()
        self.return_to_gui("reinitialize_dashboard", self.user)

    def clear_frame(self):
        frames = [
            self.main_frame,
            self.image_frame,
        ]
        for frame in frames:
            frame.pack_forget()
        self.logger.log('Cleared mood registration frame')
