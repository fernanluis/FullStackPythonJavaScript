from django.shortcuts import render
from django import forms
# To redirect user after successfull submission, we need some more imports
from django.urls import reverse
from django.http import HttpResponseRedirect

class FormNewTask(forms.Form):
    task = forms.CharField(label="New Task")

# we'll deleting our global variable
# tasks = ["foo", "bar", "baz"] now we´ll to work with sessions.

# Create your views here.
def index(request):
# check if already exist "task" key into our session
    if "tasks" not in request.session:
# if it is not, create a new list
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
#       "tasks": tasks
        "tasks": request.session["tasks"]
    })


# Add a new task, part od this will commented because we'll work with sessions

def add(request):
# check if the method is POST
    if request.method == "POST":
# Take the data the user submitted and save it as a form
        form = FormNewTask(request.POST)
# Check if the form date is valid. (server side)
        if form.is_valid():
# Isolate the task by getting a clean version of data.
                task = form.cleaned_data["task"]
# Add a new task to our task list
#               "-- tasks.append(task) --" this had been commented to work with sessions
                request.session["tasks"] += [task]
# Redirect user to tasks list
                return HttpResponseRedirect(reverse("tasks:index"))
        else:
# If the form is invalid, render the page again with the existing data.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": FormNewTask()
    })
