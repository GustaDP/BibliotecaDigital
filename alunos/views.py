from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bibliotecarias.models import Livro
from emprestimos.models import Emprestimo
from collections import Counter

@login_required
def home_aluno(request):
    return render(request, 'alunos/home_aluno.html')

@login_required
def lista_livros(request):
    livros = Livro.objects.filter(disponivel=True).order_by('titulo')
    return render(request, 'emprestimos/lista_livros.html', {'livros': livros})

@login_required
def pegar_emprestimo(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if livro.disponivel:
        Emprestimo.objects.create(aluno=request.user, livro=livro)
        livro.disponivel = False
        livro.save()
    return redirect('lista_livros')

@login_required
def meus_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(aluno=request.user).order_by('-data_emprestimo')
    return render(request, 'emprestimos/meus_emprestimos.html', {'emprestimos': emprestimos})

def recomendacoes_aluno(request):
    usuario = request.user
    emprestimos = Emprestimo.objects.filter(aluno=usuario).select_related('livro')
    if not emprestimos.exists():
        livros_recomendados = Livro.objects.filter(disponivel=True).order_by('?')[:5]
        categoria_preferida = None
    else:
        categorias_lidas = emprestimos.values_list('livro__categoria', flat=True)
        categoria_preferida = Counter(categorias_lidas).most_common(1)[0][0]

        livros_lidos_ids = emprestimos.values_list('livro_id', flat=True)
        livros_recomendados = (
            Livro.objects.filter(categoria=categoria_preferida, disponivel=True)
            .exclude(id__in=livros_lidos_ids)
            .order_by('?')[:5]
        )
    contexto = {
        'livros_recomendados': livros_recomendados,
        'categoria_preferida': categoria_preferida,
    }

    return render(request, 'alunos/recomendacoes.html', contexto)