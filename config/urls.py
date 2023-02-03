# config/urls.py

# Import django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Todo
    path('', include('apps.todo.urls', namespace='todo')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
