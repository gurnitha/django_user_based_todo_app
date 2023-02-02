# apps/todo/urls.py

# Import django modules
from django.urls import path

# Import from locals
from apps.todo import views  

app_name = 'todo'

urlpatterns = [
    path('', views.task_list_view, name='task_list_view'),
]
