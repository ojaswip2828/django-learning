# Django Migrations

## What are Migrations?

Django migrations are files that keep the database schema synchronized with the models defined in `models.py`.

Whenever a model is created, modified, or deleted, Django generates migration files that describe these changes and later applies them to the database.

---

## Why are Migrations Needed?

Without migrations, changes made in `models.py` would not automatically update the database.

Migrations allow developers to:

- Create new database tables
- Modify existing tables
- Add or remove fields
- Keep the database synchronized with models
- Track database schema changes over time

---

## Migration Workflow

```
models.py
      │
      ▼
python manage.py makemigrations
      │
      ▼
Migration File (0001_initial.py)
      │
      ▼
python manage.py migrate
      │
      ▼
Database Updated
```

---

# makemigrations

Command:

```bash
python manage.py makemigrations
```

### Purpose

- Detects changes in `models.py`
- Creates migration files
- Does **not** modify the database

Example:

If you create:

```python
class GeeksModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
```

Running:

```bash
python manage.py makemigrations
```

creates a file similar to:

```
0001_initial.py
```

This file contains instructions for creating the database table.

---

# migrate

Command:

```bash
python manage.py migrate
```

### Purpose

- Reads migration files
- Applies the changes to the database
- Creates or updates database tables

After running `migrate`, the database is updated according to the models.

---

# Example Workflow

### Step 1: Create a model

```python
from django.db import models

class GeeksModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
```

---

### Step 2: Generate Migration

```bash
python manage.py makemigrations
```

Output:

```
Migrations for 'projectApp':
    migrations/0001_initial.py
```

---

### Step 3: Apply Migration

```bash
python manage.py migrate
```

Output:

```
Applying projectApp.0001_initial... OK
```

The database table is now created.

---

# Migration Files

Migration files are stored inside:

```
projectApp/
    migrations/
        __init__.py
        0001_initial.py
```

Each migration file records changes made to the database schema.

Example:

```python
operations = [
    migrations.CreateModel(
        name='GeeksModel',
        fields=[
            ('id', models.BigAutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
            ('description', models.TextField()),
        ],
    ),
]
```

---

# Difference Between makemigrations and migrate

| makemigrations | migrate |
|---------------|---------|
| Detects model changes | Updates the database |
| Creates migration files | Executes migration files |
| Does not modify database | Modifies database schema |

---

# Advantages of Migrations

- Keeps database synchronized with models
- Tracks database changes
- Easy to revert changes if required
- Works across different database systems
- Supports team collaboration

---

# Interview Questions

### What is a migration?

A migration is a file that contains instructions for updating the database schema based on changes made in Django models.

### What does `makemigrations` do?

It detects changes in models and creates migration files without modifying the database.

### What does `migrate` do?

It reads migration files and applies those changes to the database.

### Why are migrations important?

They keep the database structure synchronized with the application's models while maintaining a history of schema changes.

---

# Key Takeaways

- Models define the database structure.
- `makemigrations` creates migration files.
- `migrate` updates the database.
- Migration files are stored inside the app's `migrations/` folder.
- Every model change should be followed by `makemigrations` and `migrate`.