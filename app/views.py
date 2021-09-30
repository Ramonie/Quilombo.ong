from django import http
from django.shortcuts import render
from django.http import request
# Create your views here.
def home (request):
    return render (request , 'index.html')

def login (request):
    return render (request, 'login.html')

def cadastro (request):
    return render ( request ,'cadastro.html')