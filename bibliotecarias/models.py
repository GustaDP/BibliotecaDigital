from django.db import models
from django.core.validators import RegexValidator

class Livro(models.Model):
    isbn_validator = RegexValidator(
        regex=r'^\d{13}$',
        message='O ISBN deve conter exatamente 13 dígitos numéricos.'
    )

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    ano_publicacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField(default=1)
    isbn = models.CharField(
        max_length=13,
        unique=True,
        validators=[isbn_validator]
    )
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

