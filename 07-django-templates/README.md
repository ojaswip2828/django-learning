

# Project 7 — Django Templates

This project demonstrates the fundamentals of **Django Templates** and the **Django Template Language (DTL)**.

The purpose of this project is to understand how Django passes data from views to HTML templates and how Django template syntax can be used to dynamically generate HTML.

---

# 1. What are Django Templates?

Django templates allow us to generate dynamic HTML by combining:

* Static HTML
* Data passed from Django views
* Django Template Language (DTL)

The basic flow is:

```text
Browser
   ↓
URL
   ↓
View
   ↓
Context Data
   ↓
Template
   ↓
HTML Response
```

For example, a view can send:

```python
context = {
    "name": "Ojaswi",
    "branch": "ECE",
    "semester": 6
}
```

The template can then display this data using:

```html
{{ name }}
{{ branch }}
{{ semester }}
```

---

# 2. Project Setup

The project was created using:

```bash
django-admin startproject template_project .
python manage.py startapp templates_app
```

The project structure is:

```text
07-django-templates/
│
├── manage.py
│
├── template_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates_app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── README.md
```

The application was added to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'templates_app',
]
```

For app-level templates, `APP_DIRS` was kept enabled:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        ...
    },
]
```

This allows Django to automatically search for templates inside the app's `templates` directory.

---

# 3. Template Variables

## Concept

Template variables are used to display data passed from a Django view.

The syntax is:

```html
{{ variable_name }}
```

Variables are passed through the context dictionary.

---

## View

In `templates_app/views.py`:

```python
from django.shortcuts import render


def variables(request):
    context = {
        "name": "Ojaswi",
        "branch": "ECE",
        "semester": 6,
    }

    return render(request, "variables.html", context)
```

Here, the context contains three variables:

```text
name
branch
semester
```

---

## Template

`variables.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Template Variables</title>
</head>
<body>

    <h1>Student Details</h1>

    <p>Name: {{ name }}</p>
    <p>Branch: {{ branch }}</p>
    <p>Semester: {{ semester }}</p>

</body>
</html>
```

Django replaces:

```html
{{ name }}
```

with:

```text
Ojaswi
```

and similarly for the other variables.

---

## URL

In `template_project/urls.py`:

```python
path("", views.variables, name="variables"),
```

The page can be accessed at:

```text
http://127.0.0.1:8000/
```

### Output

![Template Variables](01_variables.png)

---

# 4. For Loop

## Concept

The `{% for %}` template tag is used to iterate through a list.

The syntax is:

```html
{% for item in items %}
    ...
{% endfor %}
```

---

## View

```python
def for_loop(request):
    subjects = [
        "Django",
        "Python",
        "SQL",
        "Computer Networks"
    ]

    return render(request, "for_loop.html", {
        "subjects": subjects
    })
```

The list is passed to the template through the context.

---

## Template

`for_loop.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>For Loop</title>
</head>

<body>

    <h1>My Subjects</h1>

    {% for subject in subjects %}
        <p>{{ subject }}</p>
    {% endfor %}

</body>
</html>
```

The loop runs once for every subject.

The output is:

```text
Django
Python
SQL
Computer Networks
```

---

## URL

```python
path("for-loop/", views.for_loop, name="for_loop"),
```

The page can be accessed at:

```text
http://127.0.0.1:8000/for-loop/
```

### Output

![For Loop](02_for_loop.png)

---

# 5. If / Else

## Concept

The `{% if %}` tag is used to perform conditional rendering.

Django supports:

```html
{% if condition %}
{% elif condition %}
{% else %}
{% endif %}
```

---

## View

```python
def if_else(request):
    marks = 75

    return render(request, "if_else.html", {
        "marks": marks
    })
```

---

## Template

`if_else.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>If Else</title>
</head>

<body>

    <h1>Result</h1>

    {% if marks >= 40 %}
        <p>Marks: {{ marks }}</p>
        <p>Result: Passed</p>
    {% else %}
        <p>Marks: {{ marks }}</p>
        <p>Result: Failed</p>
    {% endif %}

</body>
</html>
```

Since:

```text
75 >= 40
```

the `if` block is executed.

The output is:

```text
Marks: 75
Result: Passed
```

---

## URL

```python
path("if-else/", views.if_else, name="if_else"),
```

### Output

![If Else](03_if_else.png)

---

# 6. Template Filters

## Concept

Template filters are used to modify or format values before displaying them.

The syntax is:

```html
{{ variable|filter }}
```

Filters can also be chained:

```html
{{ variable|filter1|filter2 }}
```

---

## Filters Demonstrated

This project demonstrates:

* `upper`
* `lower`
* `title`
* `length`
* `default`

---

## View

```python
def filters(request):
    context = {
        "name": "ojaswi",
        "subjects": [
            "Django",
            "Python",
            "SQL",
            "Computer Networks"
        ],
        "nickname": "",
    }

    return render(request, "filters.html", context)
```

---

## Template

`filters.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Template Filters</title>
</head>

<body>

    <h1>Template Filters</h1>

    <p>Original: {{ name }}</p>

    <p>Uppercase: {{ name|upper }}</p>

    <p>Lowercase: {{ name|lower }}</p>

    <p>Title: {{ name|title }}</p>

    <p>Number of subjects: {{ subjects|length }}</p>

    <p>
        Nickname:
        {{ nickname|default:"No nickname" }}
    </p>

</body>
</html>
```

### Explanation

#### `upper`

```html
{{ name|upper }}
```

Converts:

```text
ojaswi
```

to:

```text
OJASWI
```

#### `lower`

```html
{{ name|lower }}
```

Converts the value to lowercase.

#### `title`

```html
{{ name|title }}
```

Converts the value to title case:

```text
Ojaswi
```

#### `length`

```html
{{ subjects|length }}
```

Returns the number of elements in the list.

Here:

```text
4
```

#### `default`

```html
{{ nickname|default:"No nickname" }}
```

If `nickname` is empty or evaluates to false, Django displays:

```text
No nickname
```

---

## URL

```python
path("filters/", views.filters, name="filters"),
```

### Output

![Template Filters](04_filters.png)

---

# 7. Template Inheritance — extends and block

## Concept

Template inheritance allows multiple pages to share a common HTML structure.

Instead of repeating the same:

```html
<html>
<head>
...
</head>

<body>
...
</body>
</html>
```

in every template, we can create a base template.

The child template then extends the base template.

---

# Base Template

Create:

```text
templates/base.html
```

The `base.html` file contains the common structure.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Django Site</title>
</head>

<body>

    <h1>My Django Website</h1>

    {% block content %}
    {% endblock %}

    <footer>
        <p>Footer</p>
    </footer>

</body>
</html>
```

The important part is:

```html
{% block content %}
{% endblock %}
```

This creates a section that child templates can replace.

---

# Child Template

`extends.html`:

```html
{% extends "base.html" %}

{% block content %}

    <h2>Home Page</h2>

    <p>
        This content comes from the child template.
    </p>

{% endblock %}
```

The child template does not need to repeat the entire HTML structure.

It simply says:

```html
{% extends "base.html" %}
```

and then provides content for:

```html
{% block content %}
```

---

## View

```python
def extends(request):
    return render(request, "extends.html")
```

---

## URL

```python
path("extends/", views.extends, name="extends"),
```

The page can be accessed at:

```text
http://127.0.0.1:8000/extends/
```

### Output

![Template Inheritance](05_extends.png)

---

# 8. Include Tag

## Concept

The `{% include %}` tag allows us to reuse another template inside the current template.

This is useful for reusable components such as:

* Navigation bars
* Footers
* Cards
* Headers

---

## Navbar Template

Create:

```text
templates/includes/navbar.html
```

```html
<nav>
    <a href="/">Home</a> |
    <a href="/for-loop/">Subjects</a> |
    <a href="/filters/">Filters</a>
</nav>

<hr>
```

---

## Main Template

`include.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Include Tag</title>
</head>

<body>

    {% include "includes/navbar.html" %}

    <h1>Include Example</h1>

    <p>
        The navbar above is loaded using the include tag.
    </p>

</body>
</html>
```

The important line is:

```html
{% include "includes/navbar.html" %}
```

Django loads the navbar template and renders it inside the current template.

---

## View

```python
def include(request):
    return render(request, "include.html")
```

---

## URL

```python
path("include/", views.include, name="include"),
```

### Output

![Include Tag](06_include.png)

---

# 9. URL Tag

## Concept

The `{% url %}` tag is used to generate URLs based on the name of a URL pattern.

Instead of hardcoding:

```html
<a href="/for-loop/">Subjects</a>
```

we can use:

```html
<a href="{% url 'for_loop' %}">Subjects</a>
```

This makes the application easier to maintain.

---

## Existing URL

In `urls.py`:

```python
path(
    "for-loop/",
    views.for_loop,
    name="for_loop"
),
```

The URL has the name:

```text
for_loop
```

---

## Template

`url_tag.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>URL Tag</title>
</head>

<body>

    <h1>URL Tag Example</h1>

    <a href="{% url 'for_loop' %}">
        Go to Subjects
    </a>

</body>
</html>
```

Django resolves:

```html
{% url 'for_loop' %}
```

to:

```text
/for-loop/
```

---

## View

```python
def url_tag(request):
    return render(request, "url_tag.html")
```

---

## URL

```python
path("url-tag/", views.url_tag, name="url_tag"),
```

### Output

![URL Tag](07_url_tag.png)

---

# 10. now and firstof Tags

Two smaller template tags were also demonstrated.

---

## `now`

The `{% now %}` tag displays the current date and time.

Example:

```html
{% now "d M Y" %}
```

This could produce:

```text
15 Aug 2026
```

---

## `firstof`

The `{% firstof %}` tag displays the first variable that is not empty or false.

For example:

```html
{% firstof nickname name "Unknown Student" %}
```

If:

```python
nickname = ""
name = "Ojaswi"
```

the output will be:

```text
Ojaswi
```

---

## View

```python
def other_tags(request):
    context = {
        "nickname": "",
        "name": "Ojaswi",
    }

    return render(request, "other_tags.html", context)
```

---

## Template

`other_tags.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Other Template Tags</title>
</head>

<body>

    <h1>Other Template Tags</h1>

    <p>
        Today's date:
        {% now "d M Y" %}
    </p>

    <p>
        Student:
        {% firstof nickname name "Unknown Student" %}
    </p>

</body>
</html>
```

---

## URL

```python
path(
    "other-tags/",
    views.other_tags,
    name="other_tags"
),
```

### Output

![Other Template Tags](08_other_tags.png)

---

# 11. For Empty

## Concept

The `{% empty %}` option can be used inside a `for` loop to display alternative content when the list is empty.

Syntax:

```html
{% for item in items %}
    ...
{% empty %}
    ...
{% endfor %}
```

---

## View

```python
def for_empty(request):
    subjects = []

    return render(request, "for_empty.html", {
        "subjects": subjects
    })
```

Here:

```python
subjects = []
```

means that the list contains no items.

---

## Template

`for_empty.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>For Empty</title>
</head>

<body>

    <h1>Subjects</h1>

    {% for subject in subjects %}
        <p>{{ subject }}</p>
    {% empty %}
        <p>No subjects found.</p>
    {% endfor %}

</body>
</html>
```

Since the list is empty, Django renders:

```html
<p>No subjects found.</p>
```

---

## URL

```python
path(
    "for-empty/",
    views.for_empty,
    name="for_empty"
),
```

### Output

![For Empty](09_for_empty.png)

---

# 12. Complete views.py

The final `views.py` contains all the examples demonstrated in this project:

```python
from django.shortcuts import render


def variables(request):
    context = {
        "name": "Ojaswi",
        "branch": "ECE",
        "semester": 6,
    }

    return render(request, "variables.html", context)


def for_loop(request):
    subjects = [
        "Django",
        "Python",
        "SQL",
        "Computer Networks"
    ]

    return render(request, "for_loop.html", {
        "subjects": subjects
    })


def if_else(request):
    marks = 75

    return render(request, "if_else.html", {
        "marks": marks
    })


def filters(request):
    context = {
        "name": "ojaswi",
        "subjects": [
            "Django",
            "Python",
            "SQL",
            "Computer Networks"
        ],
        "nickname": "",
    }

    return render(request, "filters.html", context)


def extends(request):
    return render(request, "extends.html")


def include(request):
    return render(request, "include.html")


def url_tag(request):
    return render(request, "url_tag.html")


def other_tags(request):
    context = {
        "nickname": "",
        "name": "Ojaswi",
    }

    return render(request, "other_tags.html", context)


def for_empty(request):
    subjects = []

    return render(request, "for_empty.html", {
        "subjects": subjects
    })
```

---

# 13. Complete urls.py

The final `template_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from templates_app import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        views.variables,
        name="variables"
    ),

    path(
        "for-loop/",
        views.for_loop,
        name="for_loop"
    ),

    path(
        "if-else/",
        views.if_else,
        name="if_else"
    ),

    path(
        "filters/",
        views.filters,
        name="filters"
    ),

    path(
        "extends/",
        views.extends,
        name="extends"
    ),

    path(
        "include/",
        views.include,
        name="include"
    ),

    path(
        "url-tag/",
        views.url_tag,
        name="url_tag"
    ),

    path(
        "other-tags/",
        views.other_tags,
        name="other_tags"
    ),

    path(
        "for-empty/",
        views.for_empty,
        name="for_empty"
    ),
]
```

---

# 14. Important Django Template Syntax

After completing this project, the main DTL syntax covered is:

## Variables

```html
{{ variable }}
```

Used to display data.

## Tags

```html
{% tag %}
```

Used for logic and template operations.

Examples:

```html
{% if %}
{% for %}
{% extends %}
{% block %}
{% include %}
{% url %}
{% now %}
{% firstof %}
```

## Filters

```html
{{ variable|filter }}
```

Used to modify or format values.

Examples:

```html
{{ name|upper }}
{{ name|lower }}
{{ name|title }}
{{ subjects|length }}
{{ nickname|default:"No nickname" }}
```

---

# 15. Key Learning

The main concept learned in this project is how Django connects Python code with HTML templates.

```text
Python View
     ↓
Context Dictionary
     ↓
Django Template
     ↓
DTL
     ↓
Dynamic HTML
```

Django templates allow us to keep **presentation logic inside templates** while keeping the main application logic inside Python views.

The project also demonstrated how templates can be reused using:

```html
{% extends %}
```

and:

```html
{% include %}
```

This reduces code duplication and makes Django applications easier to maintain.

---

# 16. Screenshots

The following screenshots demonstrate the implementations completed in this project:

| No. | Concept              | Screenshot          |
| --- | -------------------- | ------------------- |
| 01  | Template Variables   | `01_variables.png`  |
| 02  | For Loop             | `02_for_loop.png`   |
| 03  | If / Else            | `03_if_else.png`    |
| 04  | Template Filters     | `04_filters.png`    |
| 05  | Template Inheritance | `05_extends.png`    |
| 06  | Include Tag          | `06_include.png`    |
| 07  | URL Tag              | `07_url_tag.png`    |
| 08  | Now + Firstof        | `08_other_tags.png` |
| 09  | For Empty            | `09_for_empty.png`  |

---

# Conclusion

This project provided a practical introduction to Django's Template System.

The main concepts covered were:

```text
Template Variables
        ↓
Template Tags
        ↓
Conditional Rendering
        ↓
Loops
        ↓
Template Filters
        ↓
Template Inheritance
        ↓
Reusable Templates
        ↓
Dynamic URLs
```

These concepts form the foundation for creating dynamic web pages in Django and will be used in later projects involving models, databases, forms, CRUD operations, and authentication.
