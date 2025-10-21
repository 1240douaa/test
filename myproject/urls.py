from django.urls import path
from . import views
urlpatterns = [
path('add/', views.add_student, name='add_student'),
path('getAll/', views.get_all_students, name='get_all_students'),
]
11. urls.py (project: myproject)
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('student/', include('students.urls')), # include your app urls
]
