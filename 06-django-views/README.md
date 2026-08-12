# Module 6 — Django Views

This module focuses on **Django Views**, which are responsible for handling HTTP requests, processing application logic, interacting with models and forms, and returning appropriate HTTP responses.

The module covers both:

- **Function-Based Views (FBVs)**
- **Class-Based Views (CBVs)**

A complete **Task Management System** was implemented to demonstrate CRUD operations using both approaches.

---

# 1. What is a Django View?

In Django's **MVT (Model-View-Template)** architecture, views act as the bridge between the application's data and the user interface.

A view:

1. Receives an HTTP request.
2. Processes the request.
3. Interacts with models/forms when required.
4. Selects or generates the appropriate response.
5. Returns an HTTP response to the browser.

Conceptually:

```text
Browser
   |
   | HTTP Request
   ↓
Django URL
   |
   ↓
View
   |
   ├── Model / Database
   |
   ├── Form
   |
   └── Template
   |
   ↓
HTTP Response
   |
   ↓
Browser