from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Livro

@login_required
def home_bibliotecaria(request):
    return render(request, 'bibliotecarias/home_bibliotecaria.html')

def eh_bibliotecaria(user):
    return user.is_staff

@login_required
@user_passes_test(eh_bibliotecaria)
def home_bibliotecaria(request):
    livros = Livro.objects.all()
    return render(request, 'bibliotecarias/home_bibliotecaria.html', {'livros': livros})

@login_required
@user_passes_test(eh_bibliotecaria)
def cadastrar_livro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        categoria = request.POST['categoria']
        ano_publicacao = request.POST['ano_publicacao']
        quantidade = request.POST['quantidade']
        disponivel = 'disponivel' in request.POST
        
        isbn = request.POST['isbn']
        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            categoria=categoria,
            ano_publicacao=ano_publicacao,
            quantidade=quantidade,
            isbn=isbn,
            disponivel=disponivel
        )
        messages.success(request, 'Livro cadastrado com sucesso!')
        return redirect('home_bibliotecaria')

    return render(request, 'bibliotecarias/cadastrar_livro.html')

@login_required
@user_passes_test(eh_bibliotecaria)
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.titulo = request.POST['titulo']
        livro.autor = request.POST['autor']
        livro.isbn = request.POST['isbn']
        livro.categoria = request.POST['categoria']
        livro.ano_publicacao = request.POST['ano_publicacao']
        livro.quantidade = request.POST['quantidade']
        livro.disponivel = 'disponivel' in request.POST
        livro.save()
        messages.success(request, 'Livro atualizado com sucesso!')
        return redirect('home_bibliotecaria')

    return render(request, 'bibliotecarias/editar_livro.html', {'livro': livro})

@login_required
@user_passes_test(eh_bibliotecaria)
def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    messages.success(request, 'Livro excluído com sucesso!')
    return redirect('home_bibliotecaria')