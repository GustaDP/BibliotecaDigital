from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_bibliotecaria, name='home_bibliotecaria'),
    path('livros/novo/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livros/editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('livros/excluir/<int:id>/', views.excluir_livro, name='excluir_livro'),
    path('alunos/', views.gerenciar_alunos, name='gerenciar_alunos'),
    path('emprestimos/', views.ver_emprestimos, name='ver_emprestimos'),
    path('livros/gerenciar/', views.gerenciar_livros, name='gerenciar_livros'),
]
