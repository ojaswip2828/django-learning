# Django Forms - Student Registration & Bulk Entry

## Project Overview

This project demonstrates the major concepts of Django Forms.

The project is a minimal Student Registration and Bulk Entry application.
It demonstrates how Django can create, render, validate, process, and save
user input using Forms, ModelForms, Formsets, and ModelFormSets.

---

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Django Templates

---

## Project Structure

10-django-forms/
│
├── manage.py
│
├── student_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── templates/
│   └── students/
│       ├── home.html
│       ├── basic_form.html
│       ├── manual_form.html
│       ├── submit_form.html
│       ├── search.html
│       ├── model_form.html
│       ├── formset.html
│       ├── modelformset.html
│       └── success.html
│
├── db.sqlite3
└── README.md

---

# Features

## 1. Basic Django Form

The project contains a normal Django Form called `StudentForm`.

It demonstrates:

- CharField
- EmailField
- IntegerField
- ChoiceField
- PasswordInput
- labels
- help text
- field validation

The form is created in:

students/forms.py

---

## 2. Automatic Form Rendering

Django provides convenient methods for rendering forms.

This project demonstrates:

```django
{{ form.as_p }}

3. Manual Form Rendering

The project also demonstrates rendering individual fields manually.

For example:

{{ form.name }}
{{ form.email }}
{{ form.age }}
{{ form.course }}
{{ form.password }}

This provides greater control over the HTML structure.

The project also demonstrates BoundField properties such as:

{{ form.name.errors }}
{{ form.name.id_for_label }}
{{ form.name.help_text }}
4. GET Method

The project contains a student search page using the GET method.

Example:

/search/?q=Ojaswi

The submitted data is accessed using:

request.GET.get("q")

The search then retrieves matching students from the database.

5. POST Method

The project demonstrates processing form submissions using POST.

Example:

if request.method == "POST":
    form = StudentForm(request.POST)

POST forms include CSRF protection:

{% csrf_token %}
6. Form Validation

Django automatically validates form fields.

For example, EmailField checks whether the entered value is a valid email address.

Custom validation is also implemented in the ModelForm.

Example:

def clean(self):
    cleaned_data = super().clean()


    name = cleaned_data.get("name")
    age = cleaned_data.get("age")


    if name and len(name.strip()) < 3:
        self.add_error(
            "name",
            "Name must contain at least 3 characters."
        )


    if age is not None and age < 17:
        self.add_error(
            "age",
            "Student must be at least 17 years old."
        )


    return cleaned_data
7. Student Model

The project contains a Student model.

class Student(models.Model):
    COURSE_CHOICES = [
        ("ECE", "Electronics and Communication"),
        ("CSE", "Computer Science"),
        ("ISE", "Information Science"),
    ]


    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(
        max_length=3,
        choices=COURSE_CHOICES
    )
    joined_date = models.DateField()
    bio = models.TextField(blank=True)


    def __str__(self):
        return self.name

The model is stored in the SQLite database.

8. ModelForm

StudentModelForm is directly connected to the Student model.

class StudentModelForm(forms.ModelForm):


    class Meta:
        model = Student
        fields = [
            "name",
            "email",
            "age",
            "course",
            "joined_date",
            "bio",
        ]

The ModelForm automatically creates form fields from the model.

When valid data is submitted:

form.save()

saves the student to the database.

9. Custom Widgets

The ModelForm demonstrates custom widgets.

For example:

widgets = {
    "name": forms.TextInput(
        attrs={
            "placeholder": "Enter your name"
        }
    ),


    "bio": forms.Textarea(
        attrs={
            "rows": 4,
            "placeholder": "Tell us about yourself"
        }
    ),


    "joined_date": forms.DateInput(
        attrs={
            "type": "date"
        }
    ),
}

Widgets control how form fields are displayed in HTML.

10. Formsets

The project demonstrates Django Formsets using:

formset_factory()

Three copies of the same StudentForm are displayed:

StudentFormSet = formset_factory(
    StudentForm,
    extra=3
)

The template uses:

{{ formset.management_form }}

to allow Django to track the forms correctly.

11. ModelFormSets

The project also demonstrates ModelFormSets.

A ModelFormSet allows multiple model-based forms to be handled together.

StudentFormSet = modelformset_factory(
    Student,
    form=StudentModelForm,
    extra=2
)

When the submitted data is valid:

formset.save()

saves multiple Student objects to the database.

12. Django Admin

The Student model is registered in Django Admin.

The admin interface provides:

Student records
Search
Course filtering
Joined-date filtering
Adding records
Editing records
Deleting records

The admin configuration uses:

list_display = (
    "name",
    "email",
    "age",
    "course",
    "joined_date",
)

Search:

search_fields = (
    "name",
    "email",
)

Filters:

list_filter = (
    "course",
    "joined_date",
)
URL Structure
URL	Purpose
/	Project Home
/basic/	Basic Django Form
/manual/	Manual Form Rendering
/submit/	POST and Validation
/search/	GET Student Search
/model-form/	ModelForm
/formset/	Formset
/model-formset/	ModelFormSet
/admin/	Django Admin
How to Run

Activate the virtual environment:

venv\Scripts\activate

Navigate to the project:

cd 10-django-forms

Run migrations:

python manage.py makemigrations
python manage.py migrate

Start the development server:

python manage.py runserver

Open:

http://127.0.0.1:8000/
Learning Outcomes

After completing this project, the following Django concepts are demonstrated:

Creating Django Forms
Django form field types
Automatic form rendering
Manual form rendering
BoundField properties
GET requests
POST requests
CSRF protection
Form validation
Custom validation
ModelForms
Custom widgets
Formsets
Management forms
ModelFormSets
Saving multiple model instances
Django Admin integration
Searching and filtering model records
Screenshots

The project screenshots are numbered as follows:

1_project_home.png
2_basic_form.png
3_manual_form.png
4_form_validation_error.png
5_successful_form_submission.png
6_get_search.png
7_model_form.png
8_model_form_success.png
9_formset_multiple_forms.png
10_modelformset_multiple_students.png
11_modelformset_success.png
12_admin_dashboard.png
13_admin_student_records.png
14_admin_search.png
15_admin_filter.png
Conclusion

This project provides a minimal practical demonstration of Django Forms.

It shows how user input can be collected using Django Forms, validated,
processed using GET and POST requests, converted into ModelForms, and
handled in groups using Formsets and ModelFormSets.

The project also demonstrates how submitted model data can be viewed,
searched, and filtered using the Django Admin interface.



### Step 22 — Check the complete project


Save `README.md`, then run:


```powershell
python manage.py check

Then:

python manage.py runserver

Open:

http://127.0.0.1:8000/