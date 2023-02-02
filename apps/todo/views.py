# apps/todo/views.py

# Import django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

# Import from locals
from apps.todo.models import Task

# Create your views here.

class TaskList(ListView):
	model = Task

