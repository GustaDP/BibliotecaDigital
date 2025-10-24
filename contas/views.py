from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CadastroForm, LoginForm
from django.contrib import messages

def home(request):
    return render(request, 'contas/home.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'contas/cadastro.html', {'form': form})

class LoginUsuario(LoginView):
    template_name = 'contas/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return '/bibliotecarias/home/'
        else:
            return '/alunos/home/'
                
def logout_usuario(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta com sucesso!")
    return redirect('login')
