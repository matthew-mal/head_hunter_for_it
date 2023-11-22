from django.shortcuts import render, get_object_or_404
from .models import Project


def projects(request):
    al_projects = Project.objects.all()
    context = {'projects': al_projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    project_obj = get_object_or_404(Project, id=pk)
    tags = project_obj.tags.all()

    return render(request, 'single-project.html', {'project': project_obj, 'tags': tags})
