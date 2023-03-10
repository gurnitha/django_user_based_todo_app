# django_user_based_todo_app
https://github.com/gurnitha/django_user_based_todo_app

Building a User-Based Todo App using Django version 4


## 01. SETUP


#### 01. Creating django project 

        Activities

        1. Create django project

        > (venv3941) λ python -V
        Python 3.9.5
        > λ virtualenv --version
        virtualenv 20.7.2 
        > λ pip --version
        pip 22.3.1 from C:\python\Python39\lib\site-packages\pip (python 3.9)


        > λ python -m venv venv3941
        > λ venv3941\Scripts\activate.bat
        > (venv3941) λ pip install django
        > (venv3941) λ django-admin --version
        4.0
        > (venv3941) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 02. Create todo app

        Activities

        1. Modified readme file
        modified:   README.md

        2. Create todo app
        (venv3941) λ mkdir apps\todo
        (venv3941) λ django-admin startapp todo apps\todo

        new file:   apps/todo/__init__.py
        new file:   apps/todo/admin.py
        new file:   apps/todo/apps.py
        new file:   apps/todo/migrations/__init__.py
        new file:   apps/todo/models.py
        new file:   apps/todo/tests.py
        new file:   apps/todo/views.py


#### 03. Register todo app to confit/settings.py

        Activities

        1. Modified readme file
        modified:   README.md

        2. Modified apps.py file
        modified:   apps/todo/apps.py

        3. Register toto app
        modified:   config/settings.py

        4. Testing
        (venv3941) λ python manage.py runserver

        DONE :)


#### 04. Creating Hello world 

        Activities

        1. Modified readme file
        modified:   README.md

        2. Create urls.py and home path
        (venv3941) λ touch apps/todo/urls.py
        new file:   apps/todo/urls.py

        3. Define task_list_view method which returs Hello World
        modified:   apps/todo/views.py

        4. Register todo/urls.py
        modified:   config/urls.py

        5. Testing
        http://127.0.0.1:8000/

        DONE :)


## 02. MODELS


#### 02.1 Creating Task model, run and apply migrations

        Activities

        1. Modified readme file
        modified:   README.md

        > (venv3941) λ python manage.py makemigrations
        > (venv3941) λ python manage.py migrate


#### 02.2 Register Task model to admin.py and create superuser

        Activities

        1. Modified readme file
        modified:   README.md

        2. Register Task model to admin.py
        modified:   apps/todo/admin.py

        3. Create superuser
        > (venv3941) λ python manage.py createsuperuser
        Username (leave blank to use 'hp'): admin
        Email address: admin@admin.com
        Password:admin
        Password (again):admin


## 03. CLASS BASED VIEWS


#### 03.1 Creating TaskListView

        Activities

        1. Modified readme file
        modified:   README.md

        2. Creating home path
        modified:   apps/todo/urls.py

        # Import from locals
        from apps.todo.views import TaskListView

        app_name = 'todo'

        urlpatterns = [
            path('', TaskListView.as_view(), name='tasks'),
        ]

        3. Creating views
        modified:   apps/todo/views.py

        from django.views.generic.list import ListView

        # Import from locals
        from apps.todo.models import Task

        # Create your views here.

        class TaskListView(ListView):
                model = Task

        4. Testing: run server and go to browser
        http://127.0.0.1:8000/

        TemplateDoesNotExist at /
        todo/task_list.html

        NOTE:

        1. It creates error
        2. Using ListView, by default it searchs for tempate name at todo/task_list.html
           it derives from the view class TaskList

        NEXT: Create template: todo/task_list.html


#### 03.2 Creating task_list template

        Activities

        1. Modified readme file
        modified:   README.md

        2. Activating django templates
        modified:   config/settings.py

        3. Create a template and add some text
        new file:   templates/todo/task_list.html

        4. Testing: refresh the browser

        DONE:)

        NEXT: Rendering some data to the template


#### 03.3 Modified Task model

        Activities

        1. Modified readme file
        modified:   README.md

        2. Modified Task model: adding more fields
        modified:   apps/todo/models.py

        class Task(models.Model):

            user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
            title = models.CharField(max_length=200)
            description = models.TextField(null=True, blank=True)
            in_progress = models.BooleanField(default=False)
            done = models.BooleanField(default=False)
            review = models.BooleanField(default=False)
            unnecessary = models.BooleanField(default=False)
            created = models.DateTimeField(auto_now_add=True)
            updated = models.DateTimeField(auto_now=True)

            def __str__(self):
                return self.title

            class Meta:
                ordering = ['-done']

        3. Run migrations
        new file:   apps/todo/migrations/0002_alter_task_options_rename_complete_task_done_and_more.py


#### 03.4 Adding template

        Activities

        1. Modified readme file
        modified:   README.md

        2. Adding template, setup static and media files
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/base.html
        new file:   templates/todo/kanban.html
        modified:   templates/todo/task_list.html

        3. Git ignore
        modified:   .gitignore


#### 03.5 Template inheritance

        Activities

        1. Modified readme file
        modified:   README.md

        2. Creating template inheritance
        new file:   templates/partials/aside.html
        new file:   templates/partials/footer.html
        modified:   templates/todo/task_list.html


## 04. TODO CRUD


#### 04.1 Rendering todos 

        Activities

        1. Modified readme file
        modified:   README.md

        2. Modified
        modified:   .gitignore

        3. Modified
        modified:   templates/base.html
        
        4. Render taks id
        modified:   templates/todo/task_list.html

        5. Removed
        deleted:    templates/partials/aside.html
        deleted:    templates/partials/footer.html

        DONE :

        NEXT: Using context_object_name


#### 04.2 Using context_object_name to render object_list

        Activities

        1. Modified readme file
        modified:   README.md

        2. Adding context_object_name
        modified:   apps/todo/views.py

        class TaskList(ListView):
                model = Task
                context_object_name = 'tasks'

        3. Rendering 'tasks'
        modified:   templates/todo/task_list.html

        {% for task in tasks %}

        DONE :)

        NEXT: TaskDetail