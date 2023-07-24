from django.shortcuts import render
from projects.models import Project


# Create your views here.
def list_projects(request):
    project_list = Project.objects.all()
    context = {
        "list_projects": project_list,
    }
    return render(request, "projects/list.html", context)