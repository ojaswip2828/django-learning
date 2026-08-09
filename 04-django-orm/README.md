# Django ORM - CRUD Operations

## Overview

This project demonstrates how to use the Django Object-Relational Mapper (ORM) to interact with a database using Python objects instead of writing raw SQL queries.

The project implements basic CRUD operations:

- Create
- Retrieve
- Filter
- Update
- Delete

## Technologies Used

- Python
- Django
- SQLite
- Django ORM

## Project Structure

```text
04-django-orm/
│
├── blog/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── project4/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── screenshots/
│   ├── 01-shell.png
│   ├── 02-insert.png
│   ├── 03-retrieve.png
│   ├── 04-filter.png
│   ├── 05-update.png
│   └── 06-delete.png
│
├── manage.py
└── README.md

## CRUD CODE
from blog.models import Blog

# CREATE
blog = Blog(
    title="Learning Django ORM",
    content="This blog was created using Django ORM.",
    views=50,
    url="https://example.com"
)
blog.save()

# RETRIEVE
Blog.objects.all()
Blog.objects.get(id=1)

# FILTER
Blog.objects.filter(views=50)

# UPDATE
blog = Blog.objects.first()
blog.views = 100
blog.save()

# DELETE
blog = Blog.objects.first()
blog.delete()
