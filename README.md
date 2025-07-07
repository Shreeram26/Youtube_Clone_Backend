# YouTube Clone Backend

This is the backend implementation for a basic YouTube Clone web application using **Django**.

It handles user authentication (register, login, logout), email verification (simulated), and a protected dashboard view.

---

## Features

- User Registration with unique email check  
- Password match validation  
- Simulated Email Verification using token  
- Login and Logout functionality  
- Protected Dashboard (only accessible after login)  
- Django Admin for managing users  
- Simple, Bootstrap-styled HTML templates for testing  

---

## Tech Stack

- Python 3.x  
- Django 5.x  
- SQLite (default database)  
- Bootstrap (via CDN)  

---

## How to Run Locally

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Shreeram26/Youtube_Clone_Backend.git
    cd Youtube_Clone_Backend
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

    Activate it:

    ```bash
    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create Superuser (for admin panel)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Available Routes

| URL Path             | Description                            |
|----------------------|----------------------------------------|
| `/`                  | Home page                              |
| `/register/`         | Register new user                      |
| `/login/`            | Login with username & password         |
| `/logout/`           | Logout the current user                |
| `/dashboard/`        | Protected dashboard (requires login)   |
| `/verify/<token>/`   | Simulated email verification           |
| `/admin/`            | Django admin panel                     |

---

## Admin Panel

- Go to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Log in with your superuser credentials

You can manage registered users and view profile verification status from here.

---
