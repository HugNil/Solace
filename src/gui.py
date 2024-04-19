from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials
import requests

cred = credentials.Certificate(r"Solace_key.json")
firebase_admin.initialize_app(cred)

WIDTH, HEIGHT = 480, 854
BACKGROUND_MAIN = '#014F86'
BACKGROUND_SECONDARY = '#89C2D9'
APP_NAME = 'Solace'

class GUI:
    def __init__(self, app) -> None:
        self.app = app
        self.app.title(APP_NAME)
        self.app.geometry(f'{WIDTH}x{HEIGHT}')
        self.app.minsize(WIDTH, HEIGHT)
        self.app.maxsize(WIDTH, HEIGHT)
        self.app.configure(bg=BACKGROUND_MAIN)
        set_appearance_mode('dark')

        self.create_frames()

        self.switch_frame(self.first_menu)


    def create_frames(self) -> None:
        self.start_frame = CTkFrame(master=self.app,
                                    fg_color=BACKGROUND_MAIN)
        self.start_frame.configure(width=WIDTH,
                                   height=HEIGHT)

        self.profile_frame = CTkFrame(master=self.app,
                                      fg_color=BACKGROUND_MAIN)
        self.profile_frame.configure(width=WIDTH,
                                     height=HEIGHT)

        self.frames = [
            self.start_frame,
            self.profile_frame
        ]

    
    def switch_frame(self, frame):
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
        
        # Creates alla the elements for the first frame
        self.email_label = CTkLabel(master=self.start_frame,
                                    text='Email',
                                    font=('Arial', 10, 'bold'),
                                    text_color='black')
        self.email_label.place(relx=0.5,
                               rely=0.5,
                               anchor='center')
        self.email_entry = CTkEntry(master=self.start_frame,
                                    width=150, height=2,
                                    fg_color='transparent',
                                    text_color='black',
                                    border_color='black')
        self.email_entry.place(relx=0.5,
                               rely=0.55,
                               anchor='center')
        
        self.login_button = CTkButton(master=self.start_frame,
                                      text='Login',
                                      corner_radius=32,
                                      fg_color='transparent',
                                      text_color='black',
                                      border_color='black',
                                      border_width=2,
                                      hover_color='white',
                                      command=lambda:
                                      self.login_handler(self.email_entry.get(), self.password_entry.get()))
        self.login_button.place(relx=0.5,
                                rely=0.75,
                                anchor='center')
        
        self.password_label = CTkLabel(master=self.start_frame,
                                       text='Password',
                                       font=('Arial', 10, 'bold'),
                                       text_color='black')
        self.password_label.place(relx=0.5,
                                  rely=0.6,
                                  anchor='center')
        self.password_entry = CTkEntry(master=self.start_frame,
                                       width=150,
                                       height=2,
                                       fg_color='transparent',
                                       text_color='black',
                                       border_color='black')
        self.password_entry.place(relx=0.5,
                                  rely=0.65,
                                  anchor='center')
        

    def profile_menu(self):
        pass
        

    def login_handler(self, email, password) -> None:
        input_data = {
        'email': email,
        'password': password,
        'returnSecureToken': True
        }

        # Replace [YOUR_API_KEY] with your actual Firebase API key
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCl5W4V73WVV6OdMAYWYvPmKGbKFLIJ6Oc"

        response = requests.post(url, json=input_data)
        response_data = response.json()

        if response.ok:
            self.token = response_data.get('idToken')
            self.switch_frame(self.profile_menu)
        else:
            print("Login failed:", response_data)


    def registration_handler(self, email, password) -> None:
        pass

        
        

app = CTk()
gui = GUI(app)
app.mainloop()