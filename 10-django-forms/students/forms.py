from django import forms
from .models import Student


class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Student Name",
        help_text="Enter your full name."
    )

    email = forms.EmailField(
        label="Email Address"
    )

    age = forms.IntegerField(
        min_value=17,
        max_value=30,
        label="Age"
    )

    course = forms.ChoiceField(
        choices=[
            ("ECE", "Electronics and Communication"),
            ("CSE", "Computer Science"),
            ("ISE", "Information Science"),
        ],
        label="Course"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password"
    )


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