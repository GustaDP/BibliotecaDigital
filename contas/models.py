from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    ra = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    ANOS = [
        ("Ensino Fundamental", [
            ('1º Ano - Fundamental', '1º Ano - Fundamental'),
            ('2º Ano - Fundamental', '2º Ano - Fundamental'),
            ('3º Ano - Fundamental', '3º Ano - Fundamental'),
            ('4º Ano - Fundamental', '4º Ano - Fundamental'),
            ('5º Ano - Fundamental', '5º Ano - Fundamental'),
            ('6º Ano - Fundamental', '6º Ano - Fundamental'),
            ('7º Ano - Fundamental', '7º Ano - Fundamental'),
            ('8º Ano - Fundamental', '8º Ano - Fundamental'),
            ('9º Ano - Fundamental', '9º Ano - Fundamental'),
        ]),
        ("Ensino Médio", [
            ('1º Ano - Médio', '1º Ano - Médio'),
            ('2º Ano - Médio', '2º Ano - Médio'),
            ('3º Ano - Médio', '3º Ano - Médio'),
        ]),
    ]

    ano_escolar = models.CharField(max_length=30, choices=ANOS, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome', 'ra', 'ano_escolar']

    def __str__(self):
        return f"{self.nome} ({self.ano_escolar})"
