# config/urls.py

# Import django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Todo
    path('', include('apps.todo.urls', namespace='todo')),
]
