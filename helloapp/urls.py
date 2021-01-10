# allow to reroute URLs
from django.urls import path
from . import views

# list of url patterns user may visit
# path(URL, FUNCTION, NAME)
urlpatterns = [
    path("", views.index, name="index"),
    # allow passing parameter, any name! /helloapp/kappa -> Hello Kappa!
    path("<str:name>", views.greet, name="greet"),
    path("pan", views.pan, name="pan")
]