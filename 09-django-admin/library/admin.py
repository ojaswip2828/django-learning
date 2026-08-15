from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "published_date",
        "isbn",
        "available",
    )

    search_fields = (
        "title",
        "author",
        "isbn",
    )

    list_filter = (
        "available",
        "published_date",
    )

    list_editable = (
        "available",
    )

    fields = (
        "title",
        "author",
        "published_date",
        "isbn",
        "pages",
        "available",
    )