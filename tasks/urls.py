from . import views
from django.urls import path

# helps differentiate same path names from this app and others when routin
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]