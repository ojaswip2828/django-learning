from django.shortcuts import render


def variables(request):
    context = {
        "name": "Ojaswi",
        "branch": "ECE",
        "semester": 6,
    }

    return render(request, "variables.html", context)


def for_loop(request):
    subjects = ["Django", "Python", "SQL", "Computer Networks"]

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
        "subjects": ["Django", "Python", "SQL", "Computer Networks"],
        "nickname": "",
    }

    return render(request, "filters.html", context)



def extends(request):
    return render(request, "extends.html")


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