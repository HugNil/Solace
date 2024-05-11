import customtkinter as ctk
from PIL import Image


class Exercise:
    def __init__(self, app, return_to_gui, user):
        self.app = app
        self.return_to_gui = return_to_gui
        self.user = user
        self.create_widgets()
        self.frames = [self.main_frame]

    def create_widgets(self):
        """
        Creates the widget for exercise.
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

    def add_back_button(self):
        self.back_button_img = Image.open('assests/back-button.png')
        self.back_button_img = ctk.CTkImage(
            self.back_button_img,
            size=(int(self.WIDTH * 0.15),
                  int(self.HEIGHT * 0.0375))
        )
        self.back_button = ctk.CTkButton(
            master=self.main_frame,
            image=self.back_button_img,
            fg_color=self.BACKGROUND_DARK,
            command=lambda: self.return_to_gui("profile", self.user),
            text='',
            width=int(self.WIDTH * 0.15),
            height=int(self.HEIGHT * 0.0375)
        )
        self.back_button.place(relx=0.85, rely=0.05, anchor='center')

    def start_breathing_exercise(self):
        self.breathing_window = ctk.CTk()
        self.breathing_window.title('Breathing Exercise')
        self.breathing_window.geometry('600x300')
        self.breathing_label = ctk.CTkLabel(self.breathing_window, text='')
        self.breathing_label.pack()
        if self.count % 4 == 0:
            self.breathing_label.configure(text='Inhale...')
        elif self.count % 4 == 1:
            self.breathing_label.configure(text='Hold...')
        elif self.count % 4 == 2:
            self.breathing_label.configure(text='Blow out...')
        elif self.count % 4 == 3:
            self.breathing_label.configure(text='Hold...')

        self.count += 1
        if self.count < 16:
            self.breathing_window.after(4000)

        start_button = ctk.CTkButton(
            self.breathing_window,
            text='Start breathing Exercise',
            command=self.breathing_sequence
        )
        start_button.pack()

    def update_progress_bar(self):
        self.progress_bar = ctk.CTkProgressBar(self.breathing_window,
                                               width=300,
                                               orientation='horizontal')
        self.progress_bar.pack()
        if self.count % 4 == 0:
            self.breathing_label.configure(text='Inhale...')
        elif self.count % 4 == 1:
            self.breathing_label.configure(text='Hold...')
        elif self.count % 4 == 2:
            self.breathing_label.configure(text='Blow out...')
        elif self.count % 4 == 3:
            self.breathing_label.configure(text='Hold...')

        self.count += 1
        if self.count < 16:
            self.breathing_window.after(4000)

    def breathing_sequence(self):
        self.count = 0
        self.update_progress_bar()