"""
Handles firebase connection
"""
import firebase_admin
from firebase_admin import credentials, firestore 

class FirebaseConnection(self):
    __init__(self):
    cred = credentials.Certificate(r"Solace_key.json")
    firebase_admin.initialize_app(cred)




def read_user_mood(self, user):
    """
    Read mood data for user
    """
    doc_ref = self.db.collection(u'users').document(user.email)
    mood_collection = doc_ref.collection(u'mood-form')
    docs = mood_collection.stream()

    mood_data = []
    for doc in docs:
        mood_data.append(doc.to_dict())

    return mood_data

fbc = FirebaseConnection()
email = '02hugo.nilsson@gmail.com'
mood_data = fbc.read_user_mood(email)

if mood_data:
    print(mood_data)

else:
    print(' No mood data found for this user')