from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_aluno, name='home_aluno'),
]
