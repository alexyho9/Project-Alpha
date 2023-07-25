from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": project_list,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project_instance = Project.objects.get(id=id)
    context = {
        "project_instance": project_instance,
    }
    return render(request, "projects/detail.html", context)
