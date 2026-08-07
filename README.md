# Login and Registration App

A full-stack web application built with Flask and MySQL that implements user authentication functionality including registration, login, and session management.

## Overview

This project demonstrates core backend development skills using Python Flask framework with a relational database. It provides a complete authentication system with secure session handling and database integration.

## Features

- User registration with validation
- Secure login system with email and password
- Session-based authentication
- User session management and logout
- MySQL database for persistent storage
- HTML templates with Jinja2 templating engine
- Flash messages for user feedback

## Technology Stack

- **Backend**: Python Flask 3.0.3
- **Database**: MySQL with mysql-connector-python 8.4.0
- **ORM**: SQLAlchemy 2.0.32
- **Templating**: Jinja2 3.1.4
- **Server**: Gunicorn
- **Additional**: Flask-SQLAlchemy, Werkzeug

## Project Structure

```
.
├── test.py                 # Main Flask application with all routes
├── requirements.txt        # Project dependencies
└── templates/              # HTML templates
    ├── login.html
    ├── register.html
    └── home.html
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure MySQL database connection in `test.py`
4. Run the application:
   ```bash
   python test.py
   ```

## Routes

- `/` - Home page (requires login)
- `/login` - Login page with POST for authentication
- `/register` - Registration page with POST for new accounts

## Database

Uses MySQL database with an `ACCOUNTS` table containing:
- `username` - User's display name
- `email` - User's email address
- `password` - User's password

## Key Skills Demonstrated

✅ Full-stack web development with Flask  
✅ Database design and SQL operations  
✅ User authentication and session management  
✅ HTML templating with Jinja2  
✅ Form handling and validation  
✅ Secure password handling  
✅ HTTP routing and request/response handling  
✅ Deployment with Gunicorn  

## License

Open Source
