from django.urls import path

from .views import (
    register,
    login_view,
    dashboard,
    logout_view,
    students,
    manage_students,
)


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path("students/", students, name="students"),
    path(
        "manage-students/",
        manage_students,
        name="manage_students",
    ),
]