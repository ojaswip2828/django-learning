# Django Models

## What is a Django Model?

A Django Model is a Python class that represents a database table. It allows developers to interact with the database using Python instead of writing SQL queries.

---

## Why Models?

- Represents a database table
- Stores application data
- Uses Django ORM
- Supports CRUD operations
- Integrates with Django Admin

---

## Example Model

```python
from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
```

---

## Explanation

- `CharField` → Stores short text
- `TextField` → Stores long text
- `ImageField` → Stores image paths
- `__str__()` → Returns a readable object name

---

## Migrations

Whenever models are created or modified:

```bash
python manage.py makemigrations
python manage.py migrate
```

### makemigrations

- Detects changes
- Creates migration files

### migrate

- Applies migrations
- Updates the database

---

## Register Model in Admin

```python
from django.contrib import admin
from .models import GeeksModel

admin.site.register(GeeksModel)
```

This makes the model available in the Django Admin panel.

---

## Common Field Types

- CharField
- TextField
- IntegerField
- BooleanField
- DateTimeField
- ImageField
- FileField

---

## Relationship Fields

- ForeignKey → Many-to-One
- OneToOneField → One-to-One
- ManyToManyField → Many-to-Many

---

## CRUD Operations

Create

```python
Model.objects.create(...)
```

Read

```python
Model.objects.all()
```

Update

```python
object.save()
```

Delete

```python
object.delete()
```

---

## Key Takeaways

- Model = Database Table
- ORM converts Python into SQL
- Fields define table columns
- Migrations synchronize models with the database
- Admin registration enables management through Django Admin
- CRUD operations are performed using the ORM