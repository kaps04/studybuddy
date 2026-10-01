from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Task

def home(request):
      tasks = Task.objects.all()
      return render(request, "tasks/home.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        priority = request.POST["priority"]
        Task.objects.create(title=title,
         priority=priority)

    return render(request, "tasks/add_task.html")

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()

    return redirect("/")
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect("/")