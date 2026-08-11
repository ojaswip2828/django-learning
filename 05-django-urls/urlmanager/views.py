from django.http import HttpResponse
from django.urls import reverse
import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from .models import UrlData
from .forms import Url

def home(request):
    return HttpResponse("Welcome to the Django URL Management Project!")


def about(request):
    return HttpResponse("This is the About page.")


def contact(request):
    return HttpResponse("This is the Contact page.")



def book_detail(request, book_id):
    return HttpResponse(f"Book details for ID: {book_id}")






def books_by_genre(request, genre):
    return HttpResponse(f"Books in the {genre} genre")


def book_by_slug(request, slug):
    return HttpResponse(f"Book page for: {slug}")


def url_info(request):
    about_url = reverse('urlmanager:about')
    contact_url = reverse('urlmanager:contact')

    return HttpResponse(
        f"About URL: {about_url}<br>"
        f"Contact URL: {contact_url}"
    )



def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)

        if form.is_valid():
            slug = ''.join(
                random.choice(string.ascii_letters)
                for _ in range(10)
            )

            url = form.cleaned_data["url"]

            new_url = UrlData(
                url=url,
                slug=slug
            )

            new_url.save()

            return redirect('/')

    else:
        form = Url()

    data = UrlData.objects.all()

    context = {
        'form': form,
        'data': data
    }

    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    data = get_object_or_404(UrlData, slug=slugs)
    return redirect(data.url)