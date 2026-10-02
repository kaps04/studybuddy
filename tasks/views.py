from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Task

from .forms import TaskForm

def home(request):
      tasks = Task.objects.all()
      return render(request, "tasks/home.html", {"tasks": tasks})



def add_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            priority = form.cleaned_data["priority"]

            Task.objects.create(
                title=title,
                priority=priority
            )

    return render(request, "tasks/add_task.html", {"form": form})
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()

    return redirect("/")
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect("/")

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        task.title = request.POST["title"]
        task.priority = request.POST["priority"]

        task.save()

        return redirect("/")

    return render(request, "tasks/edit_task.html", {"task": task})