from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]
