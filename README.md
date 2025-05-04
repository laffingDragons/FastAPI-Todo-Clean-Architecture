
# FastAPI Authentication and User Management

This project demonstrates a FastAPI-based backend system for user authentication and management. It includes features like user registration, login, password change, and token authentication. 

## Features

- User Registration
- User Authentication
- Password Change
- JWT Token-based Authentication
- Rate Limiting
- SQLAlchemy ORM for Database Operations

## Requirements

To run this project, you need the following dependencies:

- Python 3.9 or higher
- FastAPI
- SQLAlchemy
- PostgreSQL (or SQLite for development)
- bcrypt
- JWT
- pydantic
- alembic
- uvicorn

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Database Configuration

1. Clone the repository and set up the database. You can configure your database in the `.env` file.

2. By default, the application is configured to use PostgreSQL. You can change the connection URL in the `.env` file.

Example `.env` file:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/cleanfastapi
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

To run the application, use Uvicorn:

```bash
uvicorn main:app --reload
```

You can now access the FastAPI documentation at `http://localhost:8000/docs`.

## Endpoints

### POST `/auth/`
- Register a new user.
- Request body:
```json
{
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "password123"
}
```

### POST `/auth/token/`
- Obtain JWT access token using user credentials.
- Request body:
```json
{
  "username": "user@example.com",
  "password": "password123"
}
```

### POST `/auth/change_password/`
- Change user password.
- Requires an authenticated user.

```json
{
  "current_password": "old_password",
  "new_password": "new_password123",
  "new_password_confirm": "new_password123"
}
```

## Logging

The application includes logging for key events, such as user registration, login, and password changes. Errors are also logged for troubleshooting.

## Rate Limiting

The application uses the `slowapi` library to limit the rate of requests. For example, user registration is limited to 5 requests per hour.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

