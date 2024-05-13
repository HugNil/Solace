import os
import customtkinter as ctk
from PIL import Image
from src.log_writer import Log_writer


class Exercise:
    def __init__(self, app, return_to_gui, user, props):
        self.app = app
        self.return_to_gui = return_to_gui
        self.user = user
        self.props = props
        self.logger = Log_writer()
        self.count = 0
        current_dir = os.getcwd()
        self.parent_dir = os.path.abspath(os.path.join(current_dir,
                                                       "../../Solace"))
        self.create_widgets()
    
    def open_file_with_check(self, parent_dir, relative_path, fallback_path):
        file_path = os.path.join(parent_dir, relative_path)
        if os.path.exists(file_path):
            return file_path
        else:
            return fallback_path

    def create_widgets(self):
        """
        Creates the widget for exercise.
        """
        self.main_frame1 = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=self.props.WIDTH,
            height=self.props.HEIGHT
        )
        self.main_frame1.pack(fill='both', expand=True)

        self.start_breathing_exercise_button = ctk.CTkButton(
            self.main_frame1,
            text="Open breathing exercise",
            command=self.start_breathing_exercise
        )

        self.frames = [self.main_frame1]
        self.add_back_button()
        self.start_breathing_exercise_button.place(relx=0.5, rely=0.5,
                                                   anchor='center')

    def create_breathing_label(self):
        initial_text = "Get ready to breathe..."
        self.breathing_label = ctk.CTkLabel(master=self.breathing_frame,
                                            text=initial_text)
        self.breathing_label.pack()

    def add_back_button(self):
        self.back_button_img = Image.open(self.open_file_with_check(
            self.parent_dir,
            'assests/back-button.png',
            'assests/back-button.png'))
        self.back_button_img = ctk.CTkImage(
            self.back_button_img,
            size=(int(self.props.WIDTH * 0.15),
                  int(self.props.HEIGHT * 0.0375))
        )
        self.back_button = ctk.CTkButton(
            master=self.main_frame1,
            image=self.back_button_img,
            fg_color=self.props.BACKGROUND_DARK,
            command=lambda: self.return_to_gui("profile", self.user),
            text='',
            width=int(self.props.WIDTH * 0.15),
            height=int(self.props.HEIGHT * 0.0375)
        )
        self.back_button.place(relx=0.85, rely=0.05, anchor='center')

    def start_breathing_exercise(self):
        self.clear_frame()
        self.create_breathing_frame()

    def create_breathing_frame(self):
        """
        Creates the frame for the breathing exercise.
        """
        self.breathing_frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.props.BACKGROUND_DARK,
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            width=self.props.WIDTH,
            height=self.props.HEIGHT
        )
        self.breathing_frame.pack(fill='both', expand=True)

        self.frames = [self.breathing_frame]
        self.add_back_button()
        self.create_breathing_label()
        self.create_progress_bar()
        self.update_progress_bar()

    def create_progress_bar(self):
        self.progress_bar = ctk.CTkProgressBar(master=self.breathing_frame,
                                               width=200, height=20)
        self.progress_bar.pack()

    def update_progress_bar(self):
        phase_duration = 4000
        phases = ['Inhale...', 'Hold...', 'Exhale...', 'Hold...']
        for phase_index in range(5):
            self.breathing_label.configure(text=phases[self.count % 4])

        if phase_index == 0:
            self.progress_bar['value'] = 0
        elif phase_index == 1:
            self.progress_bar['value'] = 25
        elif phase_index == 2:
            self.progress_bar['value'] = 50
        elif phase_index == 3:
            self.progress_bar['value'] = 75

        self.count += 1

        if self.count < 16:
            self.breathing_frame.after(phase_duration,
                                       self.update_progress_bar)
        else:
            self.count = 0

    def clear_frame(self):
        """
        Clears the frame
        """
        for frame in self.frames:
            frame.pack_forget()
        self.logger.log('Cleared exercise frame')
