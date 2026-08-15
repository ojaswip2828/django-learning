from django.urls import path
from .views import home, boolean_operators, for_loop, if_else

urlpatterns = [
    path("", home, name="home"),
    path("boolean/", boolean_operators, name="boolean"),
    path("for-loop/", for_loop, name="for_loop"),
    path("if-else/", if_else, name="if_else"),
]