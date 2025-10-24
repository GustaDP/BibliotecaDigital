from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'ano_publicacao', 'quantidade', 'disponivel')
    search_fields = ('titulo', 'autor', 'categoria')
