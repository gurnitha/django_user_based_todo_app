# apps/todo/urls.py

# Import django modules
from django.urls import path

# Import from locals
from apps.todo.views import TaskList

app_name = 'todo'

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
]
