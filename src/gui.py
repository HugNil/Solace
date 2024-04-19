from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials
import requests

cred = credentials.Certificate(r"Solace_key.json")
firebase_admin.initialize_app(cred)

WIDTH, HEIGHT = 480, 854
BACKGROUND_DARK = '#014F86'
BACKGROUND_LIGHT = '#89C2D9'
BUTTON_COLOR = '#A9D6E5'
APP_NAME = 'Solace'

class GUI:
    def __init__(self, app) -> None:
        self.app = app
        self.app.title(APP_NAME)
        self.app.geometry(f'{WIDTH}x{HEIGHT}')
        self.app.minsize(WIDTH, HEIGHT)
        self.app.maxsize(WIDTH, HEIGHT)
        self.app.configure(bg=BACKGROUND_DARK)
        set_appearance_mode('dark')

        self.logo_icon_img = Image.open('assests/Solace logo1_klippt.png')
        self.logo_icon_img.thumbnail((65, 65))
        self.logo_icon = ImageTk.PhotoImage(self.logo_icon_img)

        self.logo_full_img = Image.open('assests/Solace logo2 trans.png')
        self.logo_full_img.thumbnail((450, 300))
        self.logo_full = ImageTk.PhotoImage(self.logo_full_img)

        self.password_visible = False

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

        self.frames = [
            self.start_frame,
            self.profile_frame
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
        
        # Full logo
        self.logo_full_img_label = CTkLabel(master=self.start_frame,
                                            image=self.logo_full,
                                            text='')
        self.logo_full_img_label.place(relx=0.5,
                                       rely=0.2,
                                       anchor='center')

        # Icon logo as home button
        self.logo_icon_label = CTkLabel(master=self.start_frame,
                                        image=self.logo_icon, text='')
        self.logo_icon_label.bind('<Button-1>',
                                  lambda e: self.switch_frame(self.first_menu))
        self.logo_icon_label.place(relx=0.075,
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
                                      command=lambda:
                                      self.registration_handler(self.email_entry.get(), self.password_entry.get()))
        self.register_button.place(relx=0.68,
                                rely=0.6,
                                anchor='center')
        
    
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
        self.logo_icon_label.bind('<Button-1>', lambda e: self.switch_frame(self.first_menu))
        self.logo_icon_label.place(relx=0.075,
                                   rely=0.05,
                                   anchor='center')
        

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