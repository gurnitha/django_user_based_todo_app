# apps/todo/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from apps.todo.models import Task

# Register your models here.


admin.site.register(Task)