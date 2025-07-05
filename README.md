# Django Expense Tracker API

A simple Django RESTful API that allows users to record, update, delete, and view their personal expenses securely. The application supports user authentication using JWT tokens and implements complete CRUD operations using SQLite and Django’s built-in ORM.

---

## Features

- User registration with a unique username.
- JWT-based user authentication.
- Create, read, update, and delete (CRUD) operations for user expenses.
- Validation of user credentials during login.
- Access and refresh token generation for persistent sessions.
- Clean, modular architecture following PEP 8 standards.
- Two user modes: **Regular User** and **Superuser**.

---

## Project Dependencies
asgiref==3.9.0
Django==5.2.4
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
PyJWT==2.9.0
sqlparse==0.5.3
tzdata==2025.2


---

##  Development Approach

- Implemented RESTful API design using Django REST Framework.
- Designed database models and serializers to manage expenses and income data.
- Created two Django apps:
  - `authentication` for user login, registration, and token management.
  - `expenses` for handling expense record operations.
- Applied abstraction by separating responsibilities into views, serializers, and models.

---

## Setup Instructions

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


## Create Superuser

To create a superuser with admin privileges, run the following command:


python manage.py createsuperuser






# 💰 Django Expense Tracker API

[![Django](https://img.shields.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.0-ff1709?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/JWT-5.5.0-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)](https://django-rest-framework-simplejwt.readthedocs.io/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

A **secure** and **scalable** Django RESTful API that allows users to record, update, delete, and view their personal expenses. Built with modern authentication using JWT tokens and implementing complete CRUD operations with SQLite and Django's built-in ORM.

---

## ✨ Features

- 🔐 **Secure Authentication**: JWT-based user authentication with access and refresh tokens
- 👤 **User Management**: User registration with unique username validation
- 💳 **Expense Management**: Complete CRUD operations for personal expenses
- 📊 **Data Validation**: Comprehensive validation for user credentials and expense data
- 🔄 **Token Management**: Persistent sessions with automatic token refresh
- 🏗️ **Clean Architecture**: Modular design following PEP 8 standards
- 👥 **User Roles**: Support for Regular Users and Superusers
- 📱 **Pagination**: Efficient data retrieval with paginated responses

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 5.2.4 | Web framework |
| **Django REST Framework** | 3.16.0 | API development |
| **Simple JWT** | 5.5.0 | JWT authentication |
| **SQLite** | Built-in | Database |
| **Python** | 3.9+ | Programming language |

---

## 📦 Project Dependencies

```txt
asgiref==3.9.0
Django==5.2.4
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
PyJWT==2.9.0
sqlparse==0.5.3
tzdata==2025.2
```

---

## 🏗️ Development Approach

- **RESTful Design**: Implemented using Django REST Framework for clean API architecture
- **Database Modeling**: Designed robust models and serializers for expense and income data
- **Modular Architecture**: Created two specialized Django apps:
  - `authentication` - User login, registration, and token management
  - `expenses` - Expense record operations and data management
- **Separation of Concerns**: Applied abstraction by separating responsibilities into views, serializers, and models
- **Code Quality**: Follows PEP 8 standards and Django best practices

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-expense-tracker-api.git
cd django-expense-tracker-api
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Your API will be available at `http://localhost:8000/`

---

## 🔑 API Endpoints

### 🔐 Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/` | Root endpoint | ❌ |
| `POST` | `/api/auth/login/` | User login | ❌ |
| `POST` | `/api/auth/register/` | User registration | ❌ |
| `POST` | `/api/auth/refresh_token/` | Refresh JWT token | ❌ |

### 💰 Expense Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/expenses/` | List all expenses (paginated) | ✅ |
| `POST` | `/api/expenses/` | Create new expense record | ✅ |
| `GET` | `/api/expenses/{id}/` | Retrieve specific expense | ✅ |
| `PUT` | `/api/expenses/{id}/` | Update existing expense | ✅ |
| `DELETE` | `/api/expenses/{id}/` | Delete expense | ✅ |

---

## 📋 API Usage Examples

### Authentication

#### User Registration
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123"
  }'
```

#### User Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "securepassword123"
  }'
```

### Expense Management

#### Create Expense
```bash
curl -X POST http://localhost:8000/api/expenses/ \
  -H "Authorization: Bearer your-access-token" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Grocery Shopping",
    "description": "Weekly groceries",
    "amount": 100.00,
    "transaction_type": "debit",
    "tax": 10.00,
    "tax_type": "flat"
  }'
```

#### Get All Expenses
```bash
curl -H "Authorization: Bearer your-access-token" \
  http://localhost:8000/api/expenses/
```

---

## 📝 Response Format

### Single Record Response
```json
{
  "id": 1,
  "title": "Grocery Shopping",
  "description": "Weekly groceries",
  "amount": 100.00,
  "transaction_type": "debit",
  "tax": 10.00,
  "tax_type": "flat",
  "total": 110.00,
  "created_at": "2025-01-01T10:00:00Z",
  "updated_at": "2025-01-01T10:00:00Z"
}
```

### List Response (Paginated)
```json
{
    "count": 7,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": "testuser",
            "title": "Freelance Payment",
            "description": "Payment received for web development project",
            "amount": "500.00",
            "transaction_type": "credit",
            "tax": "10.00",
            "tax_type": "percentage",
            "created_at": "2025-07-05",
            "updated_at": "2025-07-05T00:40:36.823289Z",
            "total": 550.0
        },
```

---

## 🌟 Acknowledgments

- Django REST Framework for the excellent API framework
- Simple JWT for secure authentication
- Django community for continuous support and documentation

---

<div align="center">
  <p>Made with ❤️ by Samuel Raj Bhat</p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>