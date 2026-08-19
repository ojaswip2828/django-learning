from django.shortcuts import render, redirect
from django.forms import formset_factory, modelformset_factory

from .forms import StudentForm, StudentModelForm
from .models import Student


def home(request):
    return render(request, "students/home.html")


def basic_form(request):
    form = StudentForm()

    return render(
        request,
        "students/basic_form.html",
        {"form": form}
    )


def manual_form(request):
    form = StudentForm()

    return render(
        request,
        "students/manual_form.html",
        {"form": form}
    )


def submit_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            return render(
                request,
                "students/success.html",
                {"message": "Form submitted successfully!"}
            )
    else:
        form = StudentForm()

    return render(
        request,
        "students/submit_form.html",
        {"form": form}
    )


def search_students(request):
    query = request.GET.get("q", "")

    students = Student.objects.filter(
        name__icontains=query
    )

    return render(
        request,
        "students/search.html",
        {
            "students": students,
            "query": query,
        }
    )


def model_form(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)

        if form.is_valid():
            form.save()
            return render(
                request,
                "students/success.html",
                {"message": "Student saved successfully!"}
            )
    else:
        form = StudentModelForm()

    return render(
        request,
        "students/model_form.html",
        {"form": form}
    )


def formset_view(request):
    StudentFormSet = formset_factory(
        StudentForm,
        extra=3
    )

    if request.method == "POST":
        formset = StudentFormSet(request.POST)

        if formset.is_valid():
            return render(
                request,
                "students/success.html",
                {"message": "All forms submitted successfully!"}
            )
    else:
        formset = StudentFormSet()

    return render(
        request,
        "students/formset.html",
        {"formset": formset}
    )


def modelformset_view(request):
    StudentFormSet = modelformset_factory(
        Student,
        form=StudentModelForm,
        extra=2
    )

    if request.method == "POST":
        formset = StudentFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            return render(
                request,
                "students/success.html",
                {"message": "Students saved successfully!"}
            )
    else:
        formset = StudentFormSet()

    return render(
        request,
        "students/modelformset.html",
        {"formset": formset}
    )