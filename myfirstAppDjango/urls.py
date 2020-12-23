from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("harry", views.harry, name="harry"),
    path("hermione", views.hermione, name="hermione"),
    path("<str:name>", views.greetings, name="greetings")
]
