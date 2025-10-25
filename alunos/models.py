from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
