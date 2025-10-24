from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_aluno(request):
    return render(request, 'alunos/home_aluno.html')
