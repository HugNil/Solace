import customtkinter as ctk
from PIL import Image
import log_writer
import collapsible_menu


class Exercise:
    def __init__(self, app, return_to_gui, user, props):
        self.app = app
        self.return_to_gui = return_to_gui
        self.user = user
        self.props = props
        self.logger = log_writer.Log_writer()
        self.create_widgets()
        self.frames = [self.main_frame1]

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

        self.frames = [self.main_frame1]

        self.add_back_button()
        self.add_collapsible_menu()
        self.start_breathing_exercise()

    def add_back_button(self):
        self.back_button_img = Image.open('assests/back-button.png')
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
            self.main_frame1,
            text='Start breathing Exercise',
            command=lambda: self.breathing_sequence()
        )
        start_button.pack()

    def update_progress_bar(self):
        self.progress_bar = ctk.CTkProgressBar(self.main_frame1,
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
            self.main_frame1.after(4000)

    def breathing_sequence(self):
        self.count = 0
        self.update_progress_bar()

    def add_collapsible_menu(self):
        self.collapsible_menu = collapsible_menu.CollapsibleMenu(
            self.props,
            self.return_to_gui,
            self.user,
            self.main_frame1
        )
        self.collapsible_menu.lower()

        self.collapsable_menu_img = Image.open('assests/menu-icon.png')
        self.collapsable_menu_img = ctk.CTkImage(
            self.collapsable_menu_img,
            size=(int(self.props.WIDTH * 0.08),
                  int(self.props.HEIGHT * 0.05))
            )
        self.collapsable_menu_img = ctk.CTkButton(
            master=self.main_frame1,
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

    def clear_frame(self):
        """
        Clears the frame
        """

        for frame in self.frames:
            frame.pack_forget()
        self.logger.log('Cleared exercise frame')
