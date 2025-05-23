# Firebase Chat App

A **basic terminal-based chat application** using Firebase Realtime Database and Python. Designed for learning and prototyping, this app demonstrates simple messaging between two users via the console.

![Chat App Screenshot](https://github.com/keyur2604/FIrebase-Chat-App/assets/168451989/f4856163-c9d3-43aa-bdb7-42f9eb7d89c5)

---

## Features

- Real-time message exchange using Firebase Realtime Database
- Simple, single-file Python implementation
- Easy to understand and extend

---

## Prerequisites

- Python 3.x
- `firebase_admin` Python package
- A Firebase project with a Realtime Database enabled
- Firebase service account credentials JSON file

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/keyur2604/FIrebase-Chat-App.git
   cd FIrebase-Chat-App
   ```

2. **Install dependencies:**
   ```sh
   pip install firebase-admin
   ```

3. **Configure Firebase:**
   - Download your Firebase service account JSON and save it in the project directory.
   - In `main.py`, update:
     ```python
     cred = credentials.Certificate("path/to/your/credentials.json")  # CHANGE THIS
     firebase_admin.initialize_app(cred, {
         'databaseURL': 'https://yourdatabase-default-rtdb.firebaseio.com/'  # CHANGE THIS
     })
     ```
     Replace `path/to/your/credentials.json` with the actual path to your credentials file, and update the database URL.

4. **Run the application:**
   ```sh
   python main.py
   ```

---

## How It Works

- The app listens for messages from a "partner" in the Firebase DB.
- When a message arrives, it is printed in the terminal and marked as read.
- You can reply directly from your terminal, and your message is sent back via Firebase.

---

## Notes

- This app is for demonstration and educational use. It does **not** provide authentication, encryption, or advanced chat features.
- To chat, another user should run a similar instance with their own credentials, writing/reading from the complementary fields in the database (e.g., `partner` and `self`).

---

## Contributing

Pull requests and suggestions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a PR.
