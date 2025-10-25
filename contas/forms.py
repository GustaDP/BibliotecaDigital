from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Digite seu nome completo'})
    )
    ra = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Digite seu RA'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-field', 'placeholder': 'Digite seu email'})
    )
    ano_escolar = forms.ChoiceField(
        choices=Usuario.ANOS,
        widget=forms.Select(attrs={'class': 'form-field'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-field', 'placeholder': 'Digite sua senha'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-field', 'placeholder': 'Confirme sua senha'})
    )

    class Meta:
        model = Usuario
        fields = ['nome', 'ra', 'email', 'ano_escolar', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # usa email como username
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-field',
            'placeholder': 'Digite seu email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-field',
            'placeholder': 'Digite sua senha'
        })
    )
