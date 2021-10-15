from django import http
from django.shortcuts import redirect, render
from django.http import request
from app.cadastro import CadastroForm
from django.http import request
from app.models import  Cadastro
#from app.publicar import PubliForm
#from app.arquivo import ArquivoForm
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
def perfil(request):
    return render(request, 'perfil.html')


def publicacao(request):
    return render(request, 'publicacao.html')
    


def sair(request):
    return render(request, 'login.html')


def publicar(request):
    #form = PubliForm(request.POST or None)
    #form = CadastroForm(request.POST or None)
    #form = ArquivoForm(request.POST or None)
    #if form.is_valid():
        #form.save()
        #return redirect('index.html')
    return render (request , 'index.html')