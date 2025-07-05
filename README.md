# Django Expense Tracker API

A simple Django RESTful API that allows users to record, update, delete, and view their personal expenses securely. The application supports user authentication using JWT tokens and implements complete CRUD operations using SQLite and Django’s built-in ORM.

---

## 🔧 Features

- User registration with a unique username.
- JWT-based user authentication.
- Create, read, update, and delete (CRUD) operations for user expenses.
- Validation of user credentials during login.
- Access and refresh token generation for persistent sessions.
- Clean, modular architecture following PEP 8 standards.
- Two user modes: **Regular User** and **Superuser**.

---

## 📦 Project Dependencies
asgiref==3.9.0
Django==5.2.4
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
PyJWT==2.9.0
sqlparse==0.5.3
tzdata==2025.2


---

## 🚀 Development Approach

- Implemented RESTful API design using Django REST Framework.
- Designed database models and serializers to manage expenses and income data.
- Created two Django apps:
  - `authentication` for user login, registration, and token management.
  - `expenses` for handling expense record operations.
- Applied abstraction by separating responsibilities into views, serializers, and models.

---

## ⚙️ Setup Instructions

### 1. Activate the Environment and Install Dependencies

pip install -r requirements.txt

### 1. Create a Python virtual environment

python -m venv .venv



🔑 API Endpoints
🔐 Authentication App
GET / → Root endpoint

POST /api/auth/login/ → Login

POST /api/auth/register/ → Register

POST /api/auth/refresh_token/ → Refresh token

Expenses App

GET /api/expenses/ → List all expenses (paginated)

POST /api/expenses/ → Create a new expense record

GET /api/expenses/{id}/ → Retrieve a specific expense

PUT /api/expenses/{id}/ → Update an existing expense

DELETE /api/expenses/{id}/ → Delete an expense


## 👤 Create Superuser

To create a superuser with admin privileges, run the following command:

```bash
python manage.py createsuperuser
