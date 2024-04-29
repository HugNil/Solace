from datetime import datetime
import customtkinter as ctk
from PIL import Image
import collapsible_menu
import log_writer



class MoodRegistration:
    """
    This class is responsible for the mood registration.

    The class is responsible for the mood registration of the user.
    It uses two sliders. One for the mood and one for the stress.
    The user can select a value between 1-10 for both sliders, which is
    then stored in variables for further use.
    """
    def __init__(self, app, props, user, return_to_gui):
        self.app = app
        self.props = props
        self.user = user
        self.return_to_gui = return_to_gui
        self.mood = 0
        self.stress = 0
        self.logger = log_writer.Log_writer()
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.create_widgets()
        self.frames = [self.main_frame]

    def create_widgets(self):
        """
        Creates the widgets for the mood registration. Such as the sliders.
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
        self.create_sliders()

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
            text='Mood Registration',
            font=('Arial', int(self.props.HEIGHT * 0.05), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK,
            justify='left'
        )
        self.feature_title.place(relx=0.4, rely=0.15, anchor='center')

        self.feature_description = ctk.CTkLabel(
            master=self.main_frame,
            text='''
Please select your current mood and stress level.
The mood slider ranges from 1-10, where 1 is the
worst mood and 10 is the best mood.

You can view a summary of your mood and stress in the
summary page.
            ''',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK,
            justify='left'
        )
        self.feature_description.place(relx=0.45, rely=0.3, anchor='center')

    def create_sliders(self):
        self.slider_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=0,
            width=int(self.props.WIDTH * 0.9),
            height=int(self.props.HEIGHT * 0.55)
        )
        self.slider_frame.place(relx=0.5, rely=0.6, anchor='center')

        self.mood_label = ctk.CTkLabel(
            master=self.slider_frame,
            text='Mood',
            font=('Arial', int(self.props.HEIGHT * 0.03), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK
        )
        self.mood_label.pack(pady=(10, 0))

        self.mood_slider_frame = ctk.CTkFrame(
            master=self.slider_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=0,
            width=int(self.props.WIDTH * 0.6),
            height=int(self.props.HEIGHT * 0.025)
        )
        self.mood_slider_frame.columnconfigure(0, weight=1)
        self.mood_slider_frame.columnconfigure(1, weight=1)
        self.mood_slider_frame.pack(pady=(10, 10), padx=10)

        self.mood_slider = ctk.CTkSlider(
            master=self.mood_slider_frame,
            orientation='horizontal',
            fg_color=self.props.BACKGROUND_DARK,
            bg_color=self.props.BACKGROUND_DARK,
            progress_color=self.props.BACKGROUND_LIGHT,
            border_color=self.props.BACKGROUND_LIGHT,
            button_color=self.props.SLIDERBUTTON,
            border_width=2,
            width=int(self.props.WIDTH * 0.6),
            height=int(self.props.HEIGHT * 0.025),
            from_=1,
            to=10,
            corner_radius=8,
            number_of_steps=9,
            command=self.update_mood
        )
        self.mood_slider.grid(row=0, column=0)

        self.mood_value = ctk.CTkLabel(
            master=self.mood_slider_frame,
            text='5',
            font=('Arial', int(self.props.HEIGHT * 0.03), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK
        )
        self.mood_value.grid(row=0, column=1, padx=(10, 0))

        self.stress_label = ctk.CTkLabel(
            master=self.slider_frame,
            text='Stress',
            font=('Arial', int(self.props.HEIGHT * 0.03), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK
        )
        self.stress_label.pack(pady=(10, 0))

        self.stress_slider_frame = ctk.CTkFrame(
            master=self.slider_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=0,
            width=int(self.props.WIDTH * 0.6),
            height=int(self.props.HEIGHT * 0.025)
        )
        self.stress_slider_frame.columnconfigure(0, weight=1)
        self.stress_slider_frame.columnconfigure(1, weight=1)
        self.stress_slider_frame.pack(pady=(10, 10), padx=10)

        self.stress_slider = ctk.CTkSlider(
            master=self.stress_slider_frame,
            orientation='horizontal',
            fg_color=self.props.BACKGROUND_DARK,
            bg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            progress_color=self.props.BACKGROUND_LIGHT,
            button_color=self.props.SLIDERBUTTON,
            border_width=2,
            width=int(self.props.WIDTH * 0.6),
            height=int(self.props.HEIGHT * 0.025),
            from_=1,
            to=10,
            corner_radius=8,
            number_of_steps=9,
            command=self.update_stress
        )
        self.stress_slider.grid(row=0, column=0,)

        self.stress_value = ctk.CTkLabel(
            master=self.stress_slider_frame,
            text='5',
            font=('Arial', int(self.props.HEIGHT * 0.03), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK
        )
        self.stress_value.grid(row=0, column=1, padx=(10, 0))

    def update_mood(self, value):
        """
        Updates the mood value on the slider.
        """
        self.mood_value.configure(text=int(value))
        self.mood = int(value)

    def update_stress(self, value):
        """
        Updates the stress value on the slider.
        """
        self.stress_value.configure(text=int(value))
        self.stress = int(value)

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

    def back(self):
        self.main_frame.destroy()
        self.return_to_gui("reinitialize_dashboard", self.user)

    def clear_frame(self):
        frames = [
            self.main_frame,
            self.image_frame,
            self.slider_frame
        ]
        for frame in frames:
            frame.pack_forget()
        self.logger.log('Cleared mood registration frame')
