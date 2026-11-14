# 🔐 Security Activity

## 📝 About the project

Authentication and security REST API built with **Flask**, implementing modern security practices such as password hashing with **bcrypt** and authentication via **JWT (JSON Web Tokens)**. The project demonstrates essential security concepts for web applications.

Great for learning:
- Authentication and authorization
- Password hashing with bcrypt
- JSON Web Tokens (JWT)
- API security best practices
- Environment variables with python-dotenv
- The Flask framework
- Automated testing

## 🚀 Technologies used

- **Python 3.x**
- **Flask 3.0.3** - Web framework
- **bcrypt 4.2.0** - Password hashing
- **PyJWT 2.9.0** - JWT token authentication
- **python-dotenv 1.0.1** - Environment variable management
- **Pytest 8.3.3** - Testing framework
- **Jinja2 3.1.4** - Template engine

## ⚙️ How to run

### Prerequisites

- Python 3.x installed
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/luisaferreirass/SecurityActivity.git
cd SecurityActivity
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip install -r requirements.txt
```

5. Set the environment variables:
```bash
# Create a .env file in the project root
SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_key_here
```

### Running the application
```bash
python app.py
```

The API will be available at: `http://localhost:5000`

### Running the tests
```bash
pytest
```

or, for more details:
```bash
pytest -v
```

## 🎯 Features

- 🔐 **User registration** with hashed passwords
- 🔑 **Login** with JWT token generation
- ✅ **Authentication** via JWT token
- 🛡️ **Protected routes** that require authentication
- 🔒 **Password hashing** with bcrypt
- 🧪 **Automated tests**

## 🛠️ Data model

### User

| Field | Type | Description |
|-------|------|-----------|
| id | Integer | Unique identifier |
| username | String | Username (unique) |
| password | String | Password hashed with bcrypt |
| email | String | User email |

## 📸 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth required |
|--------|----------|-----------|--------------|
| POST | `/register` | Registers a new user | No |
| POST | `/login` | Authenticates the user and returns a JWT | No |
| GET | `/profile` | Returns the logged-in user's data | Yes (JWT) |

## 💡 Usage examples

### Register a new user
```bash
POST /register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Usuário criado com sucesso",
  "user_id": 1
}
```

### Log in
```bash
POST /login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "message": "Login realizado com sucesso"
}
```

### Access a protected route
```bash
GET /profile
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com"
}
```

## 🔒 Security Features

- **Bcrypt**: Password hashing with automatic salt
- **JWT**: Stateless tokens for authentication
- **Environment variables**: Protection of sensitive credentials
- **Data validation**: User input checks
- **Protected routes**: Authentication middleware

## ⚠️ Best Practices Implemented

- Passwords are never stored in plain text
- Environment variables for sensitive information
- JWT tokens with expiration
- Input data validation
- Separation of concerns

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👩‍💻 Author

Developed by [Luisa Ferreira](https://github.com/luisaferreirass)
