from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project-object/<uuid:pk>/', views.project, name='project'),
    path('create-project/', views.create_project, name='create_project'),
    path('update-project/<uuid:pk>/', views.update_project, name='project_update'),
    path('delete-project/<uuid:pk>/', views.delete_project, name='delete_project'),
    path('tag/<slug:tag_slug>', views.filter_projects_by_tag, name='projects_by_tag'),

]
