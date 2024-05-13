import customtkinter as ctk
from PIL import Image
import collapsible_menu
import log_writer
import firebase_connection
from graph import Graph
from datetime import timedelta, datetime
import numpy as np


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
        self.add_update_button()

    def add_back_button(self):
        """
        Creates the back button feature.
        """
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
        self.feature_description.place(relx=0.350, rely=0.235, anchor='center')

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

    def add_update_button(self):
        self.update_button = ctk.CTkButton(
            master=self.image_frame,
            text='  Show past 7 days  ',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.2),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=self.show_past_seven)
        self.update_button.place(relx=0.5, rely=0.76, anchor='center')

    def add_graph(self):
        self.graph = Graph(self.image_frame, self.props)
        self.graph.display()

    def show_past_seven(self):
        """
        Get the user data from the database.
        """
        recent_docs = self.firebase.read_past_seven(
            self.user.email, 'mood-form')
        print(recent_docs)
        mood_value, stress_values = self.extract_data(recent_docs)
        self.graph.plot_data(mood_value, stress_values)

    def extract_data(self, data):
        """
        Extract the data from the recent_docs.

        """
        dates = sorted(data.keys())
        mood_values = []
        stress_values = []

        start_date = datetime.strptime(dates[0], '%Y-%m-%d')
        end_date = datetime.strptime(dates[-1], '%Y-%m-%d')

        current_date = start_date
        while current_date <= end_date:
            date_str = current_date.strftime('%Y-%m-%d')

            if date_str in data and data[date_str]:
                moods = [
                    entry['mood']
                    for entry in data[date_str]
                    if 'mood' in entry]
                stresses = [
                    entry['stress']
                    for entry in data[date_str]
                    if 'stress' in entry]

                mood_avg = int(np.mean(moods)) if moods else None
                stress_avg = int(np.mean(stresses)) if stresses else None
            else:
                mood_avg = None
                stress_avg = None

            mood_values.append(mood_avg)
            stress_values.append(stress_avg)

            current_date += timedelta(days=1)
        print(mood_values, stress_values)

        return mood_values[-7:], stress_values[-7:]

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
