# Django Project MVT Structure

## Overview

Django follows the **MVT (Model-View-Template)** architecture to organize web applications. It separates the application into different components, making the code easier to manage, maintain, and scale.

---

## MVC vs MVT

| MVC | Django (MVT) |
|-----|--------------|
| Model | Model |
| View | Template |
| Controller | View |

**Note:** Django itself manages the controller functionality through URL routing and request handling.

---

# Components of MVT

## 1. Model

The **Model** is responsible for managing the application's data.

### Responsibilities
- Defines database tables using `models.py`
- Stores application data
- Performs Create, Read, Update and Delete (CRUD) operations
- Uses Django ORM to interact with the database
- Creates database changes through migrations

---

## 2. View

The **View** handles requests from the user and contains the application's logic.

### Responsibilities
- Receives HTTP requests
- Processes business logic
- Retrieves or updates data using Models
- Sends data to Templates
- Returns an HTTP response

Views can be:
- Function-Based Views
- Class-Based Views

---

## 3. Template

The **Template** is responsible for displaying information to the user.

### Responsibilities
- Defines webpage layout using HTML
- Displays dynamic data
- Uses Django Template Language (DTL)
- Supports:
  - Variables
  - Loops
  - Conditions
  - Filters
  - Template Tags

---

# MVT Workflow

1. User sends a request from the browser.
2. Django checks the URL using `urls.py`.
3. The request reaches a View.
4. The View interacts with the Model if data is needed.
5. The View sends data to a Template.
6. The Template generates HTML.
7. Django returns the HTML response to the browser.

---

# Django Project Structure

A Django project contains several important files.

## manage.py

Command-line utility used to:

- Run the server
- Create apps
- Run migrations
- Open Django shell
- Execute project management commands

Example:

```bash
python manage.py help