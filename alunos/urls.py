from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_aluno, name='home_aluno'),
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros/pegar/<int:livro_id>/', views.pegar_emprestimo, name='pegar_emprestimo'),
    path('meus-emprestimos/', views.meus_emprestimos, name='meus_emprestimos'),
    path('recomendacoes/', views.recomendacoes_aluno, name='recomendacoes_aluno'),
]
