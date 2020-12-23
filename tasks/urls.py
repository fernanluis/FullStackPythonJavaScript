from django.urls import path
from . import views

app_name = "tasks" # con esto modificamos los enlaces del layout
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
