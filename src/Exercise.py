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

        self.prepare_label = ctk.CTkLabel(master=self.main_frame1,
                                          text="Get ready to relax...",
                                          font=('Helvetica', 16))
        self.prepare_label.pack(side='top', pady=(150, 60))

        self.start_breathing_exercise_button = ctk.CTkButton(
            master=self.main_frame1,
            text='  Open breathing Exercise',
            font=('Arial', int(self.props.HEIGHT * 0.02)),
            width=int(self.props.WIDTH * 0.5),
            corner_radius=32,
            fg_color=self.props.BUTTON_COLOR,
            text_color='black',
            border_color=self.props.BACKGROUND_LIGHT,
            border_width=2,
            hover_color='white',
            command=self.start_breathing_exercise
        )
        self.start_breathing_exercise_button.place(relx=0.5, rely=0.5,
                                                   anchor='center')

        self.frames = [self.main_frame1]
        self.add_back_button(self.main_frame1, 'profile')

    def create_breathing_label(self):
        initial_text = "Get ready to breathe..."
        self.breathing_label = ctk.CTkLabel(master=self.breathing_frame,
                                            text=initial_text,
                                            font=('Helvetica', 16))
        self.breathing_label.pack()
        self.breathing_label.pack(side='top', pady=(150, 60))

    def add_back_button(self, frame, place):
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
            master=frame,
            image=self.back_button_img,
            fg_color=self.props.BACKGROUND_DARK,
            command=lambda: self.return_to_gui(place, self.user),
            text='',
            width=int(self.props.WIDTH * 0.15),
            height=int(self.props.HEIGHT * 0.0375)
        )
        self.back_button.place(relx=0.85, rely=0.05, anchor='center')

    def start_breathing_exercise(self):
        self.count = 0
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
        self.create_breathing_label()
        self.create_progress_bar()
        self.add_back_button(self.breathing_frame, 'exercise')
        self.update_progress_bar()

    def create_progress_bar(self):
        self.progress_bar = ctk.CTkProgressBar(master=self.breathing_frame,
                                               width=200, height=20,
                                               determinate_speed=0.33,
                                               mode='determinate'
                                               )
        self.progress_bar.set(0)
        self.progress_bar.pack()
        self.progress_bar.pack(side='top', pady=30)

    def update_progress_bar(self):
        """
        Four stages of breathing exercise.
        Breathe in, hold, breathe out, hold.
        The text should change to match the stage.
        and the progress bar should update 25% each stage.
        each stage lasts 4 seconds.
        """

        self.progress_bar.stop()
        phase_duration = 4000
        phases = ['Breathe in', 'Hold', 'Breathe out', 'Hold']
        # values = [0.25, 0.50, 0.75, 1]

        # Uppdatera label och progress bar baserat på nuvarande count
        self.breathing_label.configure(text=phases[self.count % 4])
        self.progress_bar.start()

        self.count += 1
        if self.count < 16:  # Kör fyra rundor av fyra faser
            self.breathing_frame.after(phase_duration,
                                       self.update_progress_bar)
        else:
            self.count = 0  # Återställ räknaren efter alla faser är genomförda

    def clear_frame(self):
        """
        Clears the frame
        """
        for frame in self.frames:
            frame.pack_forget()
        self.logger.log('Cleared exercise frame')
