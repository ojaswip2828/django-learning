from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            password = form.cleaned_data["password"]
            user.set_password(password)

            user.save()

            messages.success(
                request,
                "Account created successfully. Please login."
            )

            return redirect("login")

    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(
            request,
            "Invalid email or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


@login_required
def dashboard(request):
    return render(
        request,
        "accounts/dashboard.html"
    )


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
@permission_required(
    "accounts.can_view_students",
    raise_exception=True
)
def students(request):
    return render(
        request,
        "accounts/students.html"
    )


@login_required
@permission_required(
    "accounts.can_manage_students",
    raise_exception=True
)
def manage_students(request):
    return render(
        request,
        "accounts/manage_students.html"
    )