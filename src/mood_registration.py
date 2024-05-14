from datetime import datetime
import os
import customtkinter as ctk
from PIL import Image
from src.collapsible_menu import CollapsibleMenu
from src.log_writer import Log_writer
from src.firebase_connection import FirebaseConnection


class MoodRegistration:
    """
    This class is responsible for the mood registration.

    The class is responsible for the mood registration of the user.
    It uses two sliders. One for the mood and one for the stress.
    The user can select a value between 1-10 for both sliders, which is
    then stored in variables for further use.
    """
    def __init__(self, app, props, user, return_to_gui):
        """
        Initializes the MoodRegistration class.

        Parameters:
        app (tk.Tk): The main application window.
        props (object): UI settings like colors and dimensions.
        user (object): The current user object.
        return_to_gui (function): Callback function to return to the main GUI.
        """
        self.app = app
        self.props = props
        self.user = user
        self.return_to_gui = return_to_gui
        self.mood = 0
        self.stress = 0
        self.logger = Log_writer()
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.firebase = FirebaseConnection()
        current_dir = os.getcwd()
        self.parent_dir = os.path.abspath(os.path.join(current_dir,
                                                       "../../Solace"))
        self.create_widgets()
        self.frames = [self.main_frame]
    
    def open_file_with_check(self, parent_dir, relative_path, fallback_path):
        file_path = os.path.join(parent_dir, relative_path)
        if os.path.exists(file_path):
            return file_path
        else:
            return fallback_path

    def create_widgets(self):
        """
        Creates the widgets for the mood registration.
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
        """
        Creates the back button image and its functionality.
        """
        self.back_button_img = Image.open(
            self.open_file_with_check(self.parent_dir,
                                      "assests/back-button.png",
                                      "assests/back-button.png"))
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
        Creates the title and description of the feature.
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
The sliders ranges from 1-10, where 1 is the
worst and 10 is the best.

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
        """
        Creates sliders for mood and stress level selection.
        """
        self.slider_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=0,
            width=int(self.props.WIDTH * 0.9),
            height=int(self.props.HEIGHT * 0.55)
        )
        self.slider_frame.place(relx=0.5, rely=0.55, anchor='center')

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
        self.mood_slider_frame.pack(pady=(0, 0), padx=10)

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
            text='2',
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
        self.stress_label.pack(pady=(5, 0))

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
        self.stress_slider_frame.pack(pady=(0, 10), padx=10)

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
            text='2',
            font=('Arial', int(self.props.HEIGHT * 0.03), 'bold'),
            text_color=self.props.BACKGROUND_LIGHT,
            fg_color=self.props.BACKGROUND_DARK
        )
        self.stress_value.grid(row=0, column=1, padx=(10, 0))

        self.mood_slider.set(2)
        self.stress_slider.set(2)

        self.submit_button = ctk.CTkButton(
            master=self.slider_frame,
            text='Submit',
            font=('Arial', int(self.props.HEIGHT * 0.03), 'bold'),
            fg_color=self.props.BACKGROUND_LIGHT,
            bg_color=self.props.BACKGROUND_DARK,
            text_color=self.props.BACKGROUND_DARK,
            command=self.submit,
            width=int(self.props.WIDTH * 0.2),
            height=int(self.props.HEIGHT * 0.05),
            hover_color=self.props.BUTTON_COLOR
        )
        self.submit_button.pack(pady=(20, 0))

    def update_mood(self, value):
        """
        Updates the mood value on the slider.
        """
        self.mood_value.configure(text=int(value))
        self.mood = int(value)

    def submit(self):
        """
        Submits the mood and stress values to the database.
        """
        self.submit_button.configure(text='Submitting...',
                                     state='disabled')
        mood_value = int(self.mood_slider.get())
        stress_value = int(self.stress_slider.get())
        print(f'Mood: {mood_value}, Stress: {stress_value}')
        email = self.user.email
        place = 'mood-form'
        data = {
            'mood': mood_value,
            'stress': stress_value
        }
        date = datetime.now().isoformat()
        self.firebase.write_to_db(
            email,
            place,
            data,
            date
        )
        self.logger.log(f'Submitted mood: {mood_value}, '
                        'stress: {stress_value}')
        self.display_confirmation()

    def display_confirmation(self):
        """
        Displays a confirmation message after submission.
        """
        self.confirmation_label = ctk.CTkLabel(
            master=self.main_frame,
            text='Mood and stress submitted!',
            font=('Arial', int(self.props.HEIGHT * 0.03), 'bold'),
            fg_color=self.props.BACKGROUND_DARK,
            text_color=self.props.BACKGROUND_LIGHT
        )
        self.confirmation_label.place(
            relx=0.5,
            rely=0.74,
            anchor='center'
            )
        self.submit_button.configure(text='Submitted!',
                                     state='disabled')

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

        self.line = Image.open(self.open_file_with_check(
            self.parent_dir,
            "assests/line-without-sides.png",
            "assests/line-without-sides.png"))
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
        self.collapsible_menu = CollapsibleMenu(
            self.props,
            self.return_to_gui,
            self.user,
            self.main_frame
        )
        self.collapsible_menu.lower()

        self.collapsable_menu_img = Image.open(self.open_file_with_check(
            self.parent_dir,
            'assests/menu-icon.png',
            'assests/menu-icon.png'))
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
        """
        Destroys the current frame and returns to the main dashboard.
        """
        self.main_frame.destroy()
        self.return_to_gui("reinitialize_dashboard", self.user)

    def clear_frame(self):
        """
        Clears all frames in the current view.
        """
        for frame in [self.main_frame, self.image_frame, self.slider_frame]:
            frame.pack_forget()
        self.logger.log('Cleared mood registration frame')
