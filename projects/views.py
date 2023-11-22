from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    """
    Отображает все добавленные проекты
    :param request:
    :return:
    """
    al_projects = Project.objects.all()
    context = {'projects': al_projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    """
    Отображает выбранный проект
    :param request:
    :param pk:
    :return:
    """
    project_obj = get_object_or_404(Project, id=pk)
    tags = project_obj.tags.all()

    return render(request, 'single-project.html', {'project': project_obj, 'tags': tags})


def create_project(request):
    """
    Создание нового проекта
    :param request:
    :return:
    """
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project_form.html', context)


def update_project(request, pk):
    """
    Обновление проекта
    :param request:
    :param pk:
    :return:
    """
    single_project = Project.objects.get(id=pk)
    form = ProjectForm(instance=single_project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=single_project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project_form.html', context)


def delete_project(request, pk):
    this_project = Project.objects.get(id=pk)
    if request.method == 'POST':
        this_project.delete()
        return redirect('projects')
    context = {'object': this_project}
    return render(request, 'delete.html', context)
