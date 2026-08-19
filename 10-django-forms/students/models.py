from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    COURSE_CHOICES = [
        ("ECE", "Electronics and Communication"),
        ("CSE", "Computer Science"),
        ("ISE", "Information Science"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    joined_date = models.DateField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name