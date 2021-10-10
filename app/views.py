from django import http
from django.shortcuts import redirect, render
from django.http import request
from app.cadastro import CadastroForm
from django.http import request
from app.models import  Cadastro


# Create your views here.
def home (request):
    return render (request , 'index.html')

def login (request):
    data = {}
    data ['db'] = Cadastro.objects.all()
    return render (request, 'login.html', data)

def cadastro (request):
    data = {}
    data['form'] = CadastroForm()
    return render ( request ,'cadastro.html', data)

def create (request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
