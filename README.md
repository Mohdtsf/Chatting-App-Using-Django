# Chatting App Using Django

This is a real-time chat application built with Django for the backend and WebSockets for real-time communication.

## Features

- User registration and authentication
- Real-time messaging between users
- Responsive design with a fixed navbar and collapsible left menu
- Storage of chat messages in the database

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

## Installation

1. **Clone the repository:**

   git clone https://github.com/Mohdtsf/Chatting-App-Using-Django.git
   cd Chatting-App-Using-Django

2. **Create and activate a virtual environment (optional but recommended):**

   python -m venv venv

   # On Windows

   venv\Scripts\activate

   # On Unix or MacOS

   source venv/bin/activate

3. **Install the required packages:** pip install -r requirements.txt

4. **Apply migrations to set up the database:** python manage.py migrate

5. **Create a superuser to access the Django admin panel:** python manage.py createsuperuser

6. **Collect static files:** python manage.py collectstatic

## Running the Application

1. **Start the development server:** python manage.py runserver

2. **Access the application:** Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Sign Up:** Register a new user account.
- **Log In:** Log in with your credentials.
- **Chat:** Select a user from the left menu to start a chat. Messages are exchanged in real-time.

## Deployment

For production deployment, consider using a production-ready web server and configuring WebSocket support appropriately. Refer to the [Django deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) for best practices.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
