"""plataforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path
from django.contrib import admin
from django.urls import path, include
from app.views import home
from app.views import login
from app.views import cadastro
from app.views import create
from app.views import perfil
from app.views import publicacao
from app.views import sair
from app.views import publicar
from app.views import informativo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'), 
    path('create/', create, name='create'),
    path('perfil/', perfil, name='perfil'),
    path('publicacao/', publicacao, name='publicacao'),
    path('sair/',sair , name='sair'),
    path('publicar/',publicar, name='publicar'),
    path('informativo/', informativo, name='informativo'),
    path('accounts/', include('allauth.urls')),
    
]

