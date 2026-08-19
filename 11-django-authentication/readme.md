# Django Authentication & Authorization System

A Django project demonstrating **custom user authentication, email-based login, user groups, custom permissions, and role-based access control (RBAC)**.

## 📌 Project Overview

This project implements a complete authentication and authorization workflow using Django.

Users can:

* Register an account
* Log in using email and password
* Access a protected dashboard
* Log out securely
* View student information based on permissions
* Manage students based on their assigned role

The project also demonstrates how Django's **Groups and Permissions** can be used to implement role-based access control.

---

## 🚀 Features

### 1. Custom User Model

The project uses Django's `AbstractUser` to create a custom user model.

Additional fields include:

* Email
* Phone number
* First name
* Last name

Email is configured as the primary authentication field.

```python
USERNAME_FIELD = "email"
```

---

### 2. User Registration

Users can create an account through a registration form.

The registration system:

* Accepts user details
* Validates the form
* Checks for duplicate emails
* Hashes the password using Django's password system
* Saves the user to the database

---

### 3. Email-Based Login

Users authenticate using:

```text
Email + Password
```

Django's `authenticate()` and `login()` functions are used to create an authenticated session.

---

### 4. Protected Dashboard

The dashboard is protected using:

```python
@login_required
```

Only authenticated users can access it.

Unauthenticated users cannot directly access protected pages.

---

### 5. Logout

Users can log out using Django's:

```python
logout(request)
```

After logout, they are redirected to the login page.

---

## 🔐 Groups & Permissions

The project demonstrates Django's authorization system using custom permissions.

Two custom permissions were created:

```text
can_view_students
can_manage_students
```

### Student

The `Student` group has:

```text
✅ Can view students
❌ Cannot manage students
```

### Student Manager

The `Student Manager` group has:

```text
✅ Can view students
✅ Can manage students
```

This creates a simple role-based access control system.

---

## 🛡️ Permission-Based Access

The student page uses:

```python
@permission_required(
    "accounts.can_view_students",
    raise_exception=True
)
```

The management page uses:

```python
@permission_required(
    "accounts.can_manage_students",
    raise_exception=True
)
```

Therefore, users cannot access pages simply by knowing their URL.

For example:

```text
Student
   ↓
/students/
   ↓
✅ Access


Student
   ↓
/manage-students/
   ↓
❌ 403 Forbidden
```

Whereas:

```text
Student Manager
   ↓
/manage-students/
   ↓
✅ Access
```

---

## 👥 Role-Based Dashboard

The dashboard also checks permissions before displaying links.

For example:

```django
{% if perms.accounts.can_view_students %}
    <a href="{% url 'students' %}">
        View Students
    </a>
{% endif %}
```

and:

```django
{% if perms.accounts.can_manage_students %}
    <a href="{% url 'manage_students' %}">
        Manage Students
    </a>
{% endif %}
```

This means users only see actions that their permissions allow.

---

## 📂 Project Structure

```text
11-django-authentication/
│
├── accounts/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── auth_project/
│   ├── settings.py
│   └── urls.py
│
├── templates/
│   └── accounts/
│       ├── register.html
│       ├── login.html
│       ├── dashboard.html
│       ├── students.html
│       └── manage_students.html
│
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **Django Templates**
* **Django Authentication System**
* **Django Groups & Permissions**

---

## ▶️ How to Run

### 1. Activate virtual environment

Windows:

```powershell
venv\Scripts\activate
```

### 2. Navigate to the project

```powershell
cd 11-django-authentication
```

### 3. Apply migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Create an admin user

```powershell
python manage.py createsuperuser
```

### 5. Start the server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 🔄 Application Flow

```text
User
 │
 ├── Register
 │      ↓
 │   Account Created
 │
 ├── Login
 │      ↓
 │   Authentication
 │      ↓
 │   Dashboard
 │
 ├── Student Role
 │      ↓
 │   View Students
 │
 └── Student Manager Role
        ↓
     View Students
        +
     Manage Students
```

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Create a custom Django User model
* Extend `AbstractUser`
* Configure `AUTH_USER_MODEL`
* Implement user registration
* Implement email-based authentication
* Use Django sessions for login/logout
* Protect views with `login_required`
* Create custom permissions
* Create and manage user groups
* Assign permissions to groups
* Implement role-based access control
* Restrict views using `permission_required`
* Conditionally display UI elements based on permissions

---

## 💡 Key Concepts

### Authentication

**Who are you?**

```text
Register → Login → Logout
```

### Authorization

**What are you allowed to do?**

```text
User → Group → Permissions → Access
```

This project demonstrates both concepts together to create a basic but functional Django authentication and authorization system.
