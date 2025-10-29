from django.urls import path
from . import views

urlpatterns = [
    path("", views.painel, name="painel_bibliotecaria"),
    path("dados/", views.dados_dashboard, name="dados_dashboard"),
]
