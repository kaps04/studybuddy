from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def home(request):
      tasks = Task.objects.all()
      return render(request, "tasks/home.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        Task.objects.create(title=title)

    return render(request, "tasks/add_task.html")