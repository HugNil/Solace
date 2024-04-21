import firebase_admin
from firebase_admin import credentials, firestore, auth
import requests
import datetime

cred = credentials.Certificate(r"Solace_key.json")
firebase_admin.initialize_app(cred)


class FirebaseConnection:
    def __init__(self):
        self.db = firestore.client()
        self.auth = auth

    
    def register_user(self, email, password):
        try:
            self.new_user = self.auth.create_user(email=email, password=password)
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
            return self.token
        else:
            print("Login failed:", response_data)
            return None
        
    
    def write_to_db(self, email, place, data, date):
        doc_ref = self.db.collection(u'users').document(email)
        mood_collection = doc_ref.collection(place) # place represents which collection to add data to, could be for example 'mood-form'
        mood_collection.document(date).set(data) # The data should be in the form of a dictionary and date makes it easier to sort data by date
    

    def read_from_db(self, email, place):
        doc_ref = self.db.collection(u'users').document(email)
        mood_collection = doc_ref.collection(place)
        docs = mood_collection.stream()

        for doc in docs:
            # This will print the document ID and the data in the form of a dictionary
            # This could be changed to return specific data or all data instead of printing it
            print(f'{doc.id} => {doc.to_dict()}')


    def test_write_read_to_db():
        data = {'mood': 4,
            'stress': 2}
        fbc = FirebaseConnection()
        email = '02hugo.nilsson@gmail.com'
        place = u'mood-form'
        date = datetime.datetime.now().isoformat()
        fbc.write_to_db(email, place, data, date)
        fbc.read_from_db(email, place)