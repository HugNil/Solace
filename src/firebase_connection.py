"""
Handles the firebase connection.
"""

import os
import firebase_admin
from firebase_admin import credentials, firestore, auth
import requests
from datetime import datetime, timedelta
from src.log_writer import Log_writer
from zoneinfo import ZoneInfo
from sys import exit

current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, "../../Solace"))
filename = "Solace_key.json"
file_path = os.path.join(parent_dir, filename)


if os.path.exists(file_path):
    print("File found at:", file_path)
    cred = credentials.Certificate(file_path)
    firebase_admin.initialize_app(cred)
elif not os.path.exists(file_path):
    cred = credentials.Certificate(r"Solace_key.json")
    firebase_admin.initialize_app(cred)
else:
    print("File not found in the parent directory")
    exit(1)



class FirebaseConnection:
    """
    Handles the firebase connection.
    """
    def __init__(self):
        """
        Initialize the connection
        """
        self.logger = Log_writer()
        self.db = firestore.client()
        self.auth = auth

    def register_user(self, email, password):
        """
        Registers a new user.
        """
        try:
            self.new_user = self.auth.create_user(email=email,
                                                  password=password)
            print(f"Successfully created user: {self.new_user.uid}")
            self.logger.log(
                f"Successfully created user: {self.new_user.uid}"
                f"with email: {email}")
            return 'success'

        except firebase_admin.auth.EmailAlreadyExistsError:
            print("Error: The user with the provided email already exists.")
            self.logger.log(
                "Error: The user with the provided email already exists.")
            return 'email_exists'

        except Exception as e:
            error_msg = e.args[0]
            if 'at least 6 characters' in error_msg:
                self.logger.log(
                    f"Error creating user: {e}")
                print("Error creating user:", e)
                return 'password_length'

    def login_user(self, email, password):
        """
        Login the user and return the token.
        """
        input_data = {
         'email': email,
         'password': password,
         'returnSecureToken': True
        }

        url = "https://identitytoolkit.googleapis.com/v1/" \
              "accounts:signInWithPassword?key=" \
              "AIzaSyCl5W4V73WVV6OdMAYWYvPmKGbKFLIJ6Oc"

        response = requests.post(url, json=input_data)
        response_data = response.json()

        if response.ok:
            self.token = response_data.get('idToken')
            return self.token
        else:
            print("Login failed:", response_data)
            return None

    def write_to_db(self, email, place, data, date):
        """
        Write the data to the database.
        """
        try:
            doc_ref = self.db.collection(u'users').document(email)
            # place represents which collection to add data to,
            # could be for example 'mood-form'
            mood_collection = doc_ref.collection(place)
            # The data should be in the form of a dictionary and
            # date makes it easier to sort data by date
            mood_collection.document(date).set(data)
            self.logger.log(f'Data written to database: {data}'
                            f'for user: {email}')
        except Exception as e:
            self.logger.log(f"Error writing to database: {e}")

    # def read_from_db(self, email, place):
    #     """
    #     Read the data from the database.
    #     """
    #     doc_ref = self.db.collection(u'users').document(email)
    #     mood_collection = doc_ref.collection(place)
    #     docs = mood_collection.stream()

    #     for doc in docs:
    #         # This will print the document ID and the
    #         # data in the form of a dictionary.
    #         #
    #         # This could be changed to return specific
    #         # data or all data instead of printing it.
    #         print(f'{doc.id} => {doc.to_dict()}')

    def read_past_seven(self, email, place):
        """
        Read the data from the last 7 days from the database,
        grouping by day and handling multiple entries per day.
        """
        timezone = ZoneInfo('Europe/Stockholm')
        now = datetime.now(timezone)
        seven_days_ago = (now - timedelta(days=6)).replace(
            hour=0, minute=0, second=0, microsecond=0)

        doc_ref = self.db.collection(u'users').document(email)
        mood_collection = doc_ref.collection(place)
        docs = mood_collection.stream()

        # Organizing documents by date
        daily_docs = {}
        for doc in docs:
            doc_data = doc.to_dict()
            doc_date = datetime.fromisoformat(
                doc.id[:-1]).replace(tzinfo=timezone)

            # Create a simple date string to use as a key
            date_key = doc_date.strftime('%Y-%m-%d')
            if doc_date >= seven_days_ago:
                if date_key not in daily_docs:
                    daily_docs[date_key] = [doc_data]
                else:
                    daily_docs[date_key].append(doc_data)

        # Fill in missing days with empty lists
        for i in range(7):
            day = (seven_days_ago + timedelta(days=i)).strftime('%Y-%m-%d')
            if day not in daily_docs:
                daily_docs[day] = []

        self.logger.log(f"Read data from the last 7 days for user: {email}")
        return daily_docs

    def test_write_read_to_db():
        """
        Test the write and read to the database.
        """
        data = {'mood': 4,
                'stress': 2}
        fbc = FirebaseConnection()
        email = '02hugo.nilsson@gmail.com'
        place = u'mood-form'
        date = datetime.datetime.now().isoformat()
        fbc.write_to_db(email, place, data, date)
        fbc.read_from_db(email, place)
