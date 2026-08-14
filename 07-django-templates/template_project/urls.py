"""
URL configuration for template_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from templates_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.variables, name="variables"),
    path("for-loop/", views.for_loop, name="for_loop"),
    path("if-else/", views.if_else, name="if_else"),
    path("filters/", views.filters, name="filters"),
    path("extends/", views.extends, name="extends"),
    path("url-tag/", views.url_tag, name="url_tag"),
    path("other-tags/", views.other_tags, name="other_tags"),
    path("for-empty/", views.for_empty, name="for_empty"),
]