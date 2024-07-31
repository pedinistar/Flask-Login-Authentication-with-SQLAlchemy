# 🛡️ Flask Login Authentication with SQLAlchemy

This project is a simple example of user registration, login, and logout functionality using Flask, Flask-SQLAlchemy, and Flask-Login. It's designed to be easy to understand and quick to implement for beginners looking to get started with Flask web development. 🌟

## 📋 Table of Contents

- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Project Structure](#project-structure-)
- [License](#license-)

## 🌟 Features

- User Registration
- User Login
- User Logout
- Secure Password Hashing

## 🚀 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flask-auth-example.git
    cd flask-auth-example
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

## 📝 Usage

- **Register a new user:** Go to `/register` and fill out the registration form.
- **Login:** After registering, log in at `/login`.
- **Access the home page:** Once logged in, visit `/home` to see the welcome message.
- **Logout:** Click the logout link to end your session.

## 📂 Project Structure

/flask_auth_app
├── app.py # Main application file
├── requirements.txt # Project dependencies
└── templates # HTML templates
├── login.html # Login page
├── register.html # Registration page
└── home.html # Home page


## 🛠️ Requirements

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug

---

Feel free to customize this project to fit your needs. Happy coding! 💻✨
