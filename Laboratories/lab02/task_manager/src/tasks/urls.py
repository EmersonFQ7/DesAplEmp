from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Página principal: lista de tareas
    path('task/new/', views.task_create, name='task_create'),  # Crear nueva tarea
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),  # Editar tarea
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Eliminar tarea
]
