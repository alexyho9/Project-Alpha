from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(False)
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "task_form": form,
    }
    return render(request, "tasks/create_task.html", context)


def my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "my_tasks": tasks,
    }
    return render(request, "tasks/my_tasks.html", context)
