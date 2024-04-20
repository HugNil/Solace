import firebase_admin
from firebase_admin import credentials, firestore, auth
import requests

cred = credentials.Certificate(r"Solace_key.json")
firebase_admin.initialize_app(cred)


class FirebaseConnection:
    def __init__(self):
        self.db = firestore.client()
        self.auth = auth

    
    def register_user(self, email, password):
        try:
            self.new_user = auth.create_user(email=email, password=password)
            print(f"Successfully created user: {self.new_user.uid}")
            return True

        except firebase_admin.auth.EmailAlreadyExistsError:
            print("Error: The user with the provided email already exists.")
            return False
            
        except Exception as e:
            print("Error creating user:", e)

    
    def login_user(self, email, password):
        input_data = {
        'email': email,
        'password': password,
        'returnSecureToken': True
        }

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCl5W4V73WVV6OdMAYWYvPmKGbKFLIJ6Oc"

        response = requests.post(url, json=input_data)
        response_data = response.json()

        if response.ok:
            self.token = response_data.get('idToken')
            return True
        else:
            print("Login failed:", response_data)
            return False