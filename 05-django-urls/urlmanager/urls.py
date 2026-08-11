from django.urls import path
from . import views

app_name = 'urlmanager'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/genre/<str:genre>/', views.books_by_genre, name='books_by_genre'),
    path('book/<slug:slug>/', views.book_by_slug, name='book_by_slug'),

    path('url-info/', views.url_info, name='url_info'),

    path('shortener/', views.urlShort, name='shortener'),
    path('u/<str:slugs>/', views.urlRedirect, name='redirect'),
]