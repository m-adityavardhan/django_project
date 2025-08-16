
# Django Project: Gamazon

Welcome to Gamazon, an e-commerce web application for games, built with Django. This project demonstrates a multi-app Django setup with user authentication, product catalog, shopping cart, and more.

## Setup Instructions

Follow these steps to set up and run the project:

### 1. Clone the Repository
```
git clone <repository-url>
cd django_project
```

### 2. Create a Virtual Environment (Recommended)
Isolates your Python dependencies for this project:
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
Installs all required Python packages (Django, Pillow, etc.):
```
pip install -r requirements.txt
```

### 4. Apply Migrations
Sets up the database tables for Django and your apps:
```
python manage.py migrate
```

### 5. (Optional) Create a Admin user
Creates an admin account for the Django admin site:
```
python manage.py createsuperuser
```
Follow the prompts to set up your admin account.

### 6. Run the Development Server
Starts the application
```
python manage.py runserver
```
Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 7. (Optional) Collect Static Files
If deploying, collect static files:
```
python manage.py collectstatic
```

---

## Features
- Game catalog with images and details
- User registration and login
- Shopping cart functionality
- Static and media file handling
- Modular Django apps for scalability

## License
This project is for educational purposes.


