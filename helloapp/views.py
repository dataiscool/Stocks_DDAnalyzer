from django.shortcuts import render
# Import ability to give http response
from django.http import HttpResponse

# Create your views here. (views.py)

# default page ""
def index(request):
    return render(request, "helloapp/index.html")

# normal /helloapp/pan
def pan(request):
    return HttpResponse("Hello, Pan!")

# passing name without html
def greetlol(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

# using django templating language: pass third parameter "context" (dictionary, can be used within  with {{name}})
def greet(request, name):
    return render(request, "helloapp/greet.html", {"name": name.capitalize()})