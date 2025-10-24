from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from bibliotecarias.models import Livro
from .models import Emprestimo
from django.shortcuts import render
from django.contrib import messages


@login_required
def pegar_emprestimo(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if livro.disponivel:
        Emprestimo.objects.create(aluno=request.user, livro=livro)
        livro.disponivel = False
        livro.save()
        messages.success(request, f'Empréstimo do livro "{livro.titulo}" realizado com sucesso!')
    else:
        messages.error(request, f'O livro "{livro.titulo}" não está disponível no momento.')
    return redirect('lista_livros')

@login_required
def devolver_livro(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id, aluno=request.user)
    if not emprestimo.devolvido:
        emprestimo.devolvido = True
        emprestimo.livro.disponivel = True
        emprestimo.livro.save()
        emprestimo.save()
        messages.success(request, f'Livro "{emprestimo.livro.titulo}" devolvido com sucesso!')
    else:
        messages.error(request, f'O livro "{emprestimo.livro.titulo}" já foi devolvido.')
    return redirect('meus_emprestimos')

@login_required
def meus_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(aluno=request.user).order_by('-data_emprestimo')
    return render(request, 'emprestimos/meus_emprestimos.html', {'emprestimos': emprestimos})

@login_required
def lista_livros(request):
    livros = Livro.objects.all().order_by('titulo')
    return render(request, 'emprestimos/lista_livros.html', {'livros': livros})

