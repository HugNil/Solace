from customtkinter import *
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from firebase_connection import FirebaseConnection
import warnings

warnings.filterwarnings("ignore", message="CTkLabel Warning: Given image is not CTkImage*")

WIDTH, HEIGHT = 480, 854
BACKGROUND_DARK = '#014F86'
BACKGROUND_LIGHT = '#89C2D9'
BUTTON_COLOR = '#A9D6E5'
APP_NAME = 'Solace'
GRADIENT = "NightTrain.json"



class GUI:
    def __init__(self, app) -> None:
        self.app = app
        self.app.title(APP_NAME)
        self.app.geometry(f'{WIDTH}x{HEIGHT}')
        self.app.minsize(WIDTH, HEIGHT)
        self.app.maxsize(WIDTH, HEIGHT)
        self.app.configure(bg=BACKGROUND_DARK)
        set_appearance_mode('dark')

        self.firebase = FirebaseConnection()

        self.logo_icon_img = Image.open('assests/menu logo.png')
        self.logo_icon_img.thumbnail((30, 30))
        self.logo_icon = ImageTk.PhotoImage(self.logo_icon_img)

        self.logo_full_img = Image.open('assests/Solace logo2 trans.png')
        self.logo_full_img.thumbnail((450, 300))
        self.logo_full = ImageTk.PhotoImage(self.logo_full_img)

        self.foregound_img = Image.open('assests/Solace_background1.png')
        self.foregound_img.thumbnail((700, 500))
        self.foreground = ImageTk.PhotoImage(self.foregound_img)

        self.copyright_img = Image.open('assests/Copyright.png')
        self.copyright_img.thumbnail((400, 200))
        self.copyright = ImageTk.PhotoImage(self.copyright_img)

        self.line_img = Image.open('assests/Line.png')
        self.line_img.thumbnail((540,440))
        self.line = ImageTk.PhotoImage(self.line_img)


        self.password_visible = False
        self.option_visible = False
        self.remember_var = tk.IntVar()
        self.remember_email = None
        self.remember_password = None
        self.remember_token = None


        self.create_frames()

        self.switch_frame(self.first_menu)


    def create_frames(self) -> None:
        # Generates the frames
        self.start_frame = CTkFrame(master=self.app,
                                    fg_color=BACKGROUND_DARK,
                                    border_color=BACKGROUND_LIGHT,
                                    border_width=2)
        self.start_frame.configure(width=WIDTH,
                                   height=HEIGHT)

        self.profile_frame = CTkFrame(master=self.app,
                                      fg_color=BACKGROUND_DARK,
                                      border_color=BACKGROUND_LIGHT,
                                      border_width=2)
        self.profile_frame.configure(width=WIDTH,
                                     height=HEIGHT)
        
        self.option_frame = CTkFrame(master=self.start_frame,
                                     fg_color=BACKGROUND_DARK,
                                     border_color=BACKGROUND_LIGHT,
                                     border_width=2,
                                     width=120,
                                     height=150)
        

        self.option_frame1 = CTkFrame(master=self.profile_frame,
                                     fg_color=BACKGROUND_DARK,
                                     border_color=BACKGROUND_LIGHT,
                                     border_width=2,
                                     width=120,
                                     height=150)


        self.frames = [
            self.start_frame,
            self.profile_frame,
            self.option_frame,
            self.option_frame1
        ]

    
    def switch_frame(self, frame):
        # Clear old frames and open the new one
        self.clear_frames()
        frame()

    
    def clear_frames(self) -> None:
        for frame in self.frames:
            frame.pack_forget()

    
    def first_menu(self):
        # Clear old frames
        self.clear_frames()

        # Opens the new first_menu
        self.start_frame.pack(fill=tk.BOTH,
                                    expand=True)
        
        self.foregound_img = CTkLabel(master=self.start_frame,
                                      image=self.foreground,
                                      text="")
        self.foregound_img.place(relx=0.5,
                                    rely=0.45,
                                    anchor='center')
        

        # Full logo
        self.logo_full_img_label = CTkLabel(master=self.start_frame,
                                            image=self.logo_full,
                                            text='')
        self.logo_full_img_label.place(relx=0.5,
                                       rely=0.175,
                                       anchor='center')
        
        #Copyright text
        self.copyright_img = CTkLabel(master=self.start_frame,
                                      image=self.copyright,
                                      text="")

        self.copyright_img.place(relx=0.43,
                                 rely=0.92,
                                 anchor="center")
        
        self.line_img = CTkLabel(master=self.start_frame,
                                 image=self.line,
                                 text="")
        
        self.line_img.place(relx=0.45,
                                 rely=0.8,
                                 anchor="center")


        # Icon logo as home button
        self.logo_icon_label1 = CTkLabel(master=self.start_frame,
                                        image=self.logo_icon, text='')
        
        #Icon logo as mini-menu 
        self.logo_icon_label1.bind("<Button-1>",
                                  command= lambda e: self.option_toggle('home'))

        
        self.logo_icon_label1.place(relx=0.075,
                                   rely=0.05,
                                   anchor='center')
        

        # Creates alla the elements for the first frame
        self.email_label = CTkLabel(master=self.start_frame,
                                    text='Email',
                                    font=('Arial', 12, 'bold'),
                                    text_color=BACKGROUND_LIGHT)
        
        self.email_label.place(relx=0.5,
                               rely=0.37,
                               anchor='center')
        self.email_entry = CTkEntry(master=self.start_frame,
                                    width=180,
                                    height=2,
                                    fg_color=BUTTON_COLOR,
                                    text_color='black',
                                    border_color=BACKGROUND_LIGHT,
                                    border_width=2)
        self.email_entry.place(relx=0.5,
                               rely=0.4,
                               anchor='center')
        
        self.login_button = CTkButton(master=self.start_frame,
                                      text='Login',
                                      corner_radius=32,
                                      fg_color=BUTTON_COLOR,
                                      text_color='black',
                                      border_color=BACKGROUND_LIGHT,
                                      border_width=2,
                                      hover_color='white',
                                      command=lambda:
                                      self.login_handler(self.email_entry.get(), self.password_entry.get()))
        self.login_button.place(relx=0.32,
                                rely=0.6,
                                anchor='center')
        
        self.password_label = CTkLabel(master=self.start_frame,
                                       text='Password',
                                       font=('Arial', 12, 'bold'),
                                       text_color=BACKGROUND_LIGHT)
        self.password_label.place(relx=0.5,
                                  rely=0.45,
                                  anchor='center')
        self.password_entry = CTkEntry(master=self.start_frame,
                                       width=180,
                                       height=2,
                                       fg_color=BUTTON_COLOR,
                                       text_color='black',
                                       border_color=BACKGROUND_LIGHT,
                                       border_width=2,
                                       show='*')
        self.password_entry.place(relx=0.5,
                                  rely=0.48,
                                  anchor='center')
        
        self.show_image = ImageTk.PhotoImage(Image.open('assests/show.png').resize((20, 20)))
        self.hide_image = ImageTk.PhotoImage(Image.open('assests/hide.png').resize((20, 20)))

        self.show_password_button = CTkLabel(master=self.start_frame,
                                         image=self.hide_image,
                                         text='')
        self.show_password_button.bind('<Button-1>', lambda e: self.toggle_show_password())
        self.show_password_button.place(relx=0.7,
                                   rely=0.465,)
        
        
        self.register_button = CTkButton(master=self.start_frame,
                                      text='Register',
                                      corner_radius=32,
                                      fg_color=BUTTON_COLOR,
                                      text_color='black',
                                      border_color=BACKGROUND_LIGHT,
                                      border_width=2,
                                      hover_color='white',
                                      command=lambda: self.register_handler(self.email_entry.get(), self.password_entry.get()))
        self.register_button.place(relx=0.68,
                                rely=0.6,
                                anchor='center')
        
        self.remember_checkbox = CTkCheckBox(master=self.start_frame,
                                             text='Remember Me',
                                             variable=self.remember_var,
                                             fg_color=BACKGROUND_LIGHT,
                                             text_color=BACKGROUND_LIGHT,
                                             hover=False,
                                             corner_radius=25,
                                             border_width=2,
                                             border_color=BACKGROUND_LIGHT,
                                             width=3,
                                             height=3)
        self.remember_checkbox.place(relx=0.5, rely=0.54, anchor='center'),
    
    

    def option_toggle(self, menu_choice):
        if menu_choice == 'home':
            if self.option_visible:
                self.option_frame.lower()
                self.option_frame.place_forget()
                self.option_visible = False
            else:
                self.option_frame.lift()
                self.option_frame.place(relx=0.075, rely=0.16, anchor='center')
                self.option_visible = True
        elif menu_choice == 'profile':
            if self.option_visible:
                self.option_frame1.lower()
                self.option_frame1.place_forget()
                self.option_visible = False
            else:
                self.option_frame1.lift()
                self.option_frame1.place(relx=0.075, rely=0.16, anchor='center')
                self.option_visible = True

        
    
    def toggle_show_password(self):
        if self.password_visible:
            self.password_entry.configure(show='*')
            self.show_password_button.configure(image=self.hide_image)
            self.password_visible = False
        else:
            self.password_entry.configure(show='')
            self.show_password_button.configure(image=self.show_image)
            self.password_visible = True
        

    def profile_menu(self):
        self.profile_frame.pack(fill=tk.BOTH,
                                    expand=True)
        
        self.logo_icon_label = CTkLabel(master=self.profile_frame,
                                         image=self.logo_icon, text='')
        self.logo_icon_label.bind('<Button-1>',
                                  lambda e: self.option_toggle('profile'))
        self.logo_icon_label.place(relx=0.075,
                                   rely=0.05,
                                   anchor='center')
        

    def login_handler(self, email, password) -> None:
        self.token = self.firebase.login_user(email, password)
        if self.token != None:
            self.remember_login()
            self.switch_frame(self.profile_menu)

    
    def remember_login(self) -> None:
        if self.remember_var.get() == 1:
            self.remember_email = self.email_entry.get()
            self.remember_password = self.password_entry.get()
            self.remember_token = self.token
            print("Remembering login")


    def register_handler(self, email, password):
        if self.firebase.register_user(email, password):
            self.switch_frame(self.profile_menu)
        
        

app = CTk()
gui = GUI(app)
app.mainloop()