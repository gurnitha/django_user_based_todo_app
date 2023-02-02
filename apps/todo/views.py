# apps/todo/views.py

# Import django modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def task_list_view(request):
	return HttpResponse('Hello World!')

