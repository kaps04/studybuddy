from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def home(request):
    tasks = Task.objects.filter(owner=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    if total_tasks > 0:
        completion_rate = round(
            (completed_tasks / total_tasks) * 100, 1
        )
    else:
        completion_rate = 0

    return render(request, "tasks/home.html", {
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_rate": completion_rate,
    
    })


   
@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect("home")
    else:
        form = TaskForm()

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
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST["title"]
        task.priority = request.POST["priority"]

        task.save()

        return redirect("/")

    return render(request, "tasks/edit_task.html", {"task": task}
                  
                )
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        "form": form
    })