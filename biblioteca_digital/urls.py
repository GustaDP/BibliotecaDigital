from django.contrib import admin
from django.urls import path, include
from contas.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contas/', include('contas.urls')),
    path('alunos/', include('alunos.urls')),
    path('bibliotecarias/', include('bibliotecarias.urls')),
    path('emprestimos/', include('emprestimos.urls')),
    path("dashboard/", include("dashboard.urls")),
]
