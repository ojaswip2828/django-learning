# Create a Django App

## Objective

Learn how to create and configure a Django application inside an existing Django project.

## Concepts Covered

- Django Project
- Django App
- startapp command
- INSTALLED_APPS
- Views
- URL Routing
- include()
- HttpResponse
- Development Server

## Project Structure

```
project2/
│
├── manage.py
├── project2/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── projectApp/
    ├── views.py
    ├── urls.py
    ├── models.py
    └── ...
```

## Output

Displays:

Hello! Welcome to my first Django App.

## Screenshots

- Project Structure
- Terminal
- Browser Output

## Commands Used

```bash
python manage.py startapp projectApp
python manage.py runserver
```