# Task Management Backend API

A Django REST Framework-based backend API for task management with user authentication. This project provides a robust foundation for building task management applications with secure user registration, login, and token-based authentication.

## 🚀 Features

- **User Authentication System**
  - User registration with email and password confirmation
  - Secure user login with token-based authentication
  - Token-based API authentication using Django REST Framework
  - Password validation and security checks

- **RESTful API Design**
  - Clean and intuitive API endpoints
  - JSON responses for easy frontend integration
  - Proper HTTP status codes and error handling
  - Django REST Framework integration

- **Security Features**
  - Token-based authentication
  - Password confirmation validation
  - Django's built-in security middleware
  - CSRF protection

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.2.6
- **API Framework**: Django REST Framework
- **Database**: SQLite (development)
- **Authentication**: Token-based authentication
- **Python Version**: Compatible with Python 3.8+

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Task_Management_backend
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Navigate to the api directory
cd api

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Endpoints

### Base URL
```
http://127.0.0.1:8000/api/auth/
```

### Available Endpoints

#### 1. **Welcome Message**
- **GET** `/auth/`
- **Description**: Welcome endpoint with API information
- **Authentication**: required
- **Response**:
```json
{
    "message": "Hi welcome the authentication api v1 here you can make register, login you can register using username, email and password and you can login using username and password"
}
```

#### 2. **User Registration**
- **POST** `/auth/register`
- **Description**: Register a new user account
- **Authentication**: Not required
- **Request Body**:
```json
{
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password",
    "confirmation": "your_password"
}
```
- **Response** (Success):
```json
{
    "token": "your_auth_token_here",
    "message": "User created successfully!"
}
```

#### 3. **User Login**
- **POST** `/auth/login`
- **Description**: Authenticate user and get access token
- **Authentication**: Not required
- **Request Body**:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
- **Response** (Success):
```json
{
    "token": "your_auth_token_here",
    "message": "Logged in successfully"
}
```

## 🔐 Authentication

This API uses token-based authentication. After successful login or registration, you'll receive an authentication token. Include this token in the `Authorization` header for protected endpoints:

```
Authorization: Bearer your_token_here
```

## 📁 Project Structure

```
Task_Management_backend/
├── api/                          # Django project directory
│   ├── api/                      # Main project configuration
│   │   ├── __init__.py
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py              # Main URL configuration
│   │   ├── wsgi.py              # WSGI configuration
│   │   └── asgi.py              # ASGI configuration
│   ├── authentication/          # Authentication app
│   │   ├── models.py            # Database models
│   │   ├── views.py             # API views
│   │   ├── serializers.py       # Data serializers
│   │   ├── urls.py              # Authentication URLs
│   │   ├── auth.py              # Custom authentication
│   │   └── migrations/          # Database migrations
│   ├── db.sqlite3               # SQLite database
│   └── manage.py                # Django management script
├── requirements.txt             # Python dependencies
└── README.md                   # This file
```

## 🧪 Testing the API

### Using cURL

#### Register a new user:
```bash
curl -X POST http://127.0.0.1:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpassword123",
    "confirmation": "testpassword123"
  }'
```

#### Login:
```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpassword123"
  }'
```

### Using Python requests:

```python
import requests

# Register
response = requests.post('http://127.0.0.1:8000/auth/register', json={
    'username': 'testuser',
    'email': 'test@example.com',
    'password': 'testpassword123',
    'confirmation': 'testpassword123'
})
print(response.json())

# Login
response = requests.post('http://127.0.0.1:8000/auth/login', json={
    'username': 'testuser',
    'password': 'testpassword123'
})
token = response.json()['token']
print(f"Token: {token}")
```

## 🔧 Configuration

### Environment Variables

The project uses `python-dotenv` for environment variable management. Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Django Settings

Key settings in `api/api/settings.py`:

- **Database**: SQLite for development
- **Authentication**: Token-based authentication
- **Time Zone**: Africa/Mogadishu
- **Language**: English (en-us)
- **Debug Mode**: Enabled for development

## 🚀 Deployment

### Production Considerations

1. **Security**:
   - Change the `SECRET_KEY` in production
   - Set `DEBUG=False`
   - Configure proper `ALLOWED_HOSTS`
   - Use environment variables for sensitive data

2. **Database**:
   - Consider using PostgreSQL or MySQL for production
   - Set up proper database migrations

3. **Static Files**:
   - Configure static file serving for production
   - Use a CDN for better performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of the CS50 Web Development course. Please refer to the course guidelines for usage and distribution.

## 🆘 Troubleshooting

### Common Issues

1. **Database Migration Errors**:
   ```bash
   python manage.py makemigrations authentication
   python manage.py migrate
   ```

2. **Token Authentication Issues**:
   - Ensure you're including the token in the `Authorization` header
   - Check that the token format is `Bearer your_token_here`

3. **Port Already in Use**:
   ```bash
   python manage.py runserver 8001
   ```

## 📞 Support

If you encounter any issues or have questions about this project, please:

1. Check the troubleshooting section above
2. Review the Django REST Framework documentation
3. Create an issue in the repository

---

**Happy Coding! 🎉**
