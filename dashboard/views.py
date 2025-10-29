from django.shortcuts import render
from datetime import date
from bibliotecarias.models import Livro
from emprestimos.models import Emprestimo
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def painel(request):
    total_livros = Livro.objects.count()
    total_usuarios = User.objects.count()
    emprestimos_ativos = Emprestimo.objects.filter(devolvido=False).count()
    livros_atrasados = Emprestimo.objects.filter(devolvido=False, data_devolucao__lt=date.today()).count()

    top_livros = (
        Emprestimo.objects.values('livro__titulo')
        .annotate(total=Count('livro'))
        .order_by('-total')[:5]
    )
    top_livros_labels = [l['livro__titulo'] for l in top_livros]
    top_livros_data = [l['total'] for l in top_livros]

    generos = (
        Livro.objects.values('categoria')
        .annotate(total=Count('categoria'))
        .order_by('-total')[:5]
    )
    generos_labels = [g['categoria'] for g in generos]
    generos_data = [g['total'] for g in generos]

    emprestimos_completos = Emprestimo.objects.filter(devolvido=True, data_devolucao__isnull=False)
    duracoes = [(e.data_devolucao - e.data_emprestimo).days for e in emprestimos_completos]
    duracao_media = sum(duracoes) / len(duracoes) if duracoes else 0

    context = {
        'total_livros': total_livros,
        'total_usuarios': total_usuarios,
        'emprestimos_ativos': emprestimos_ativos,
        'livros_atrasados': livros_atrasados,
        'top_livros_labels': top_livros_labels,
        'top_livros_data': top_livros_data,
        'generos_labels': generos_labels,
        'generos_data': generos_data,
        'duracao_media': round(duracao_media, 1),
        'ano_atual': date.today().year,
    }

    return render(request, 'dashboard/painel.html', context)

def dados_dashboard(request):
    total_livros = Livro.objects.count()
    total_alunos = Aluno.objects.count()
    total_emprestimos = Emprestimo.objects.count()
    emprestimos_ativos = Emprestimo.objects.filter(devolvido=False).count()

    dados = {
        "total_livros": total_livros,
        "total_alunos": total_alunos,
        "total_emprestimos": total_emprestimos,
        "emprestimos_ativos": emprestimos_ativos,
    }
    return JsonResponse(dados)

