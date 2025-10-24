from django.db import models
from django.conf import settings
from bibliotecarias.models import Livro

class Emprestimo(models.Model):
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.livro.titulo} - {self.aluno.username}"
