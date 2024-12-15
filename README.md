# User Authentication System

[Live Demo](https://auth-app-production-754b.up.railway.app/)

This is a Django-based user authentication system with features for login, signup, forgot password, change password, dashboard, and user profile. The app supports user login via **username or email**, and includes access restrictions to certain pages based on user authentication.

## Features

- **User Authentication** with **username** or **email** and **password**.
- Pages for **login**, **signup**, **forgot password**, **change password**, **dashboard**, and **profile**.
- Restrict access to certain pages based on authentication status.
  
## Requirements

- Django (Version: 3.0+)
- Python 3.x

## Pages and Functionality

### 1. Login Page
- **Fields**: Username/Email and Password.
- Includes links for **Sign Up** and **Forgot Password**.
- Authentication is performed on this page to log the user in.

### 2. Sign Up Page
- **Fields**: Username, Email, Password, and Confirm Password.
- Includes a link to go back to the **Login Page** if the user already has an account.
- After successful signup, the user is logged in automatically.

### 3. Forgot Password Page
- **Field**: Email.
- A button to send a password reset email to the user.
- Upon clicking the button, an email with a link to reset the password is sent to the provided email address.

### 4. Change Password Page
- **Authentication Required**: This page can only be accessed by authenticated users.
- **Fields**: Old Password, New Password, and Confirm Password.
- Includes a button to go back to the **Dashboard**.
- After successfully changing the password, the user is redirected to the dashboard.

### 5. Dashboard
- **Accessible to authenticated users only**.
- Displays a greeting message, such as "Hi, username!".
- Includes links to the **Profile Page** and **Change Password** page.
- Provides an option to **logout**.

### 6. Profile Page
- **Fields displayed**: Username, Email, Date Joined, and Last Updated.
- Includes a link to go back to the **Dashboard**.
- Provides an option to **logout**.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/shubham3451/Auth-app/
```

### 2. Install dependencies
Navigate to your project directory and create a virtual environment:

```bash
cd your-repository-name
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure the database
Run the following commands to create and apply database migrations:

```bash
python manage.py migrate
```

### 4. Create a superuser (optional)
If you want to create an admin user to manage the site:

```bash
python manage.py createsuperuser
```

### 5. Start the development server
Run the development server:

```bash
python manage.py runserver
```

The app will be accessible at `http://127.0.0.1:8000/`.


## Authentication Flow

1. **Sign Up**: User provides their username, email, and password to create a new account. After submission, they are automatically logged in and redirected to the dashboard.
2. **Login**: User provides their username/email and password to log in to the app.
3. **Forgot Password**: User enters their email address to receive instructions on how to reset their password.
4. **Change Password**: User can change their password after logging in by providing their old and new passwords.
5. **Dashboard**: The authenticated user is greeted by their username and has the option to go to their profile or change their password.
6. **Profile**: Displays the user's personal information, including their username, email, and account creation date.
