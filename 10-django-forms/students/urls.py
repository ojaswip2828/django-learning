from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("basic/", views.basic_form, name="basic_form"),
    path("manual/", views.manual_form, name="manual_form"),
    path("submit/", views.submit_form, name="submit_form"),
    path("search/", views.search_students, name="search_students"),
    path("model-form/", views.model_form, name="model_form"),
    path("formset/", views.formset_view, name="formset"),
    path("model-formset/", views.modelformset_view, name="model_formset"),
]