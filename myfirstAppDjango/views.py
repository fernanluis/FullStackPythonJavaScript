from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# django templates - plantillas
# def index(request):
#    return HttpResponse('Hello World!')

def index(request):
    #return HttpResponse('<h1 style=\"color:blue\">Hello World!</h1>')
    return render(request, "helloApp/index.html")

def harry(request):
    return HttpResponse('Hello World!')

def hermione(request):
    return HttpResponse('Hello World!')

def greetings(request, name):
    #return HttpResponse(f'Hi {name.capitalize()}!')
    return render(request, "helloApp/greetings.html", {"name":name.capitalize()})
