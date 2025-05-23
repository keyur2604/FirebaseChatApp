import firebase_admin
from firebase_admin import credentials, db
import time
cred = credentials.Certificate("path/to/your/credentials.json") #CHANGE THIS TO YOUR CREDS JSON FILE
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://yourdatabase-default-rtdb.firebaseio.com/' #CHANGE THIS TO YOUR DATABASE URL
})
ref = db.reference('/chat')
def listen_for_messages():
    while True:
        partner_message = ref.child('partner').get()
        if partner_message is not None and partner_message != '#':
            print("Partner:", partner_message)
            ref.child('partner').set('#')
            reply = input("Your reply: ")
            send_reply(reply)

def send_reply(reply):
    ref.child('self').set(reply)
def main():
    print("Chat application started!")
    listen_for_messages()

main()
