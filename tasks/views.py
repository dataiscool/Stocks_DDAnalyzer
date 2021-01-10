from django.shortcuts import render
# using django forms api
from django import forms
# to redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

# tasks (global variable not good since every1 will have the same. remove and use sessions)
tasks = ["leetcode", "project", "stream"]

# class to create forms
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# default page
def index(request):
    # Check if already a session if tasks key present
    if "tasks" not in request.session:
        # If not, create new list
        # Django stores session data inside a table, so we must create a table by running "python manage.py migrate"
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })

# add new tasks
def add(request):
    # server-side validation, for when response is sent back.
    # when going to this page, it's GET, so won't activate.
    # validate if method is POST
    if request.method == "POST":
         # Store data user submitted as a form
         form = NewTaskForm(request.POST)
         # Validate form (server-side)
         if form.is_valid():
            # Our form has values task and priority, we getting the task value
            task = form.cleaned_data["task"]
            # Add new task to list
            request.session["tasks"] += [task]
            # Redirect to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))
         else:
            # If form is invalid, re-render page with existing info
            return render(request, "tasks/add.html", {
                "form" : form
            })
    
    # Used for GET requests; when accessing this page (not form submission)
    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    })