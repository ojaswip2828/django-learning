# Django Model Data Types and Fields

## Introduction

Model fields define the type of data stored in a database table. Every field in a Django model becomes a column in the database.

Model fields are responsible for:

- Defining the database column type.
- Validating user input.
- Determining the default form widget.
- Applying constraints and field options.

> Avoid using reserved names such as `save`, `delete`, or `clean` as field names because they conflict with Django's built-in model methods.

---

# Example

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

In this example:

- `CharField` stores text values.
- `IntegerField` stores integer numbers.
- `DateField` stores dates.
- `ForeignKey` creates a relationship between the Album and Musician models.

After creating the models, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

to create the corresponding database tables.

---

# Viewing Database Tables

Open the database shell:

```bash
python manage.py dbshell
```

Useful SQLite commands:

```sql
.tables
.schema musician
.schema album
```

These commands display all tables and their structure.

---

# Common Django Model Fields

## AutoField

An auto-incrementing integer field used as the default primary key.

---

## BigAutoField

A 64-bit auto-incrementing integer field used for large primary key values.

---

## BigIntegerField

Stores large integer values.

---

## BinaryField

Stores raw binary data.

---

## BooleanField

Stores either `True` or `False`.

---

## CharField

Stores short text such as names, titles, or addresses.

Requires the `max_length` attribute.

Example:

```python
name = models.CharField(max_length=100)
```

---

## DateField

Stores only the date.

Example:

```python
birth_date = models.DateField()
```

---

## DateTimeField

Stores both date and time.

---

## DecimalField

Stores fixed-precision decimal numbers.

Useful for prices and financial calculations.

---

## DurationField

Stores time durations.

---

## EmailField

Stores and validates email addresses.

---

## FileField

Stores uploaded files.

---

## FloatField

Stores floating-point numbers.

---

## ImageField

Stores uploaded image files.

Requires the Pillow library.

---

## IntegerField

Stores integer values.

---

## GenericIPAddressField

Stores IPv4 or IPv6 addresses.

---

## PositiveIntegerField

Stores positive integers including zero.

---

## PositiveSmallIntegerField

Stores small positive integers.

---

## SlugField

Stores URL-friendly text consisting of letters, numbers, hyphens, and underscores.

Example:

```
my-first-blog
```

---

## SmallIntegerField

Stores small integer values.

---

## TextField

Stores large amounts of text.

Commonly used for descriptions and articles.

---

## TimeField

Stores only the time.

---

## URLField

Stores and validates URLs.

---

## UUIDField

Stores universally unique identifiers (UUIDs).

Useful for generating unique IDs that are difficult to guess.

---

# Summary

Django provides many built-in field types for storing different kinds of data. Choosing the appropriate field ensures proper validation, efficient storage, and better database design. Each field automatically maps to the corresponding database column type and integrates with Django's ORM and form system.