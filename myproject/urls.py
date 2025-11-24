from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Une simple vue inline pour la page d'accueil
def home(request):
    return HttpResponse("<h1>Bienvenue sur mon site Django 🎉</h1><p>Ceci est la page d'accueil.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # <-- Ajout de la page d'accueil
    path('student/', include('students.urls')),  # Si ton app students a un fichier urls.py
]
