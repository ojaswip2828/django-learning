from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "age",
        "course",
        "joined_date",
    )

    search_fields = (
        "name",
        "email",
    )

    list_filter = (
        "course",
        "joined_date",
    )