# django_expense_tracker_api

A simple Django/Pythoon RESTful API allows users to record, manipulate, remove personal expensese and keeps  the information secured from other.

 This projects has wll four database operation i.e. CREATE, READ, UPDATE & DELETE using SQLite databse and django built-in db model to create database schemas.

## Features

- User Registration with unique username only.
- User Authentication on JWT based while logging in.
- Creade, View, Update, & Deletion of  user records.
- User Credentials validation before  login.
- Token generation for extended period of serverside connection and token refresh- refresh features.
- Clean and modular architecture follows PEP 8 uer proper documentation.
- Two user modes: **Regular users** & **Superuser**

## Project Setup & Requirements
asgiref==3.9.0
Django==5.2.4
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
PyJWT==2.9.0
sqlparse==0.5.3
tzdata==2025.2



# Approach on Developing this project
- Implement RESTful API to for api programming
- Use of Schema class and database model class for database dessign and data serialization of the user expenses and incmome records,
- All users must be registered first inorder to use the application.
- Develop this project with two apps , authentictaion app for  handling all the endpoints in auth subgroup and expenses for hanling the youth minisnrty.
- Design database table as per the given requirements by including all the given fields and their respective data types.
- Apply abstraction by using different components to build the application together.


### Importnt steps to create this project

# Create python virtua environment
 python -m venev .venv

# Install dependencies
pip install -r requirements.txt

# Create Project
django-admin startproject expense_tracker_api

# Create Django Aaps
python manage.py startapp authentication
python manage.py expenses

# Cofigure installed apps in settings.py
Add name of apps in settings.py

### Folder Structure

expense_tracker_app/
├── authentication/      
├── expenses/            
│   ├── serializers/
│   └── views/
├── expense_tracker_app/
├── manage.py
└── README.md

 ### API Endpoints
 Authentication App
 - 1. '/' root 
 - 2. 'api/auth/login.' login
 - 3. 'api/auth/register/, register
 - 4. 'api/auth/refresh_token' refresh_token

 Expenses App
- 1. 'GET/expenses' list by pagination
- 2' 'POST/expenses' create new record
- 3 . 'GET/expenses' Ciew cepficif user records by id,
- 4 . 'PUT/expenses' Update specific user recorrd
- 5 . 'DELETE/expenses' Delete user records as per the amry

## To create SuperUser in this app
- You can use Django-admin builtin superuser features to access elevated permission

# Go to root directory where the django projects is located at & run following command

python manage.py createsuperuser
