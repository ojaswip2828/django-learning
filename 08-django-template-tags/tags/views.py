from django.shortcuts import render


def home(request):
    return render(request, "tags/home.html")


def boolean_operators(request):
    context = {
        "age": 21,
        "marks": 85,
        "name": "Ojaswi",
        "courses": ["Python", "Django", "SQL"],
    }
    return render(request, "tags/boolean.html", context)


def for_loop(request):
    context = {
        "students": ["Ojaswi", "Rahul", "Ananya", "Karan"],
        "points": [(1, 2), (3, 4), (5, 6)],
        "student_info": {
            "Name": "Ojaswi",
            "Branch": "ECE",
            "CGPA": 8.43,
        },
    }
    return render(request, "tags/for_loop.html", context)


def if_else(request):
    context = {
        "marks": 85,
        "attendance": 82,
        "has_backlogs": False,
        "status": True,
        "optional_data": None,
    }
    return render(request, "tags/if_else.html", context)