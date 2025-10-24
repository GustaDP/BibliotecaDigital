from django.urls import path
from . import views

urlpatterns = [
    path('livros/pegar/<int:livro_id>/', views.pegar_emprestimo, name='pegar_emprestimo'),
    path('livros/devolver/<int:emprestimo_id>/', views.devolver_livro, name='devolver_livro'),
    path('meus-emprestimos/', views.meus_emprestimos, name='meus_emprestimos'),
]
