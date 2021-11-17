from django.db import models
from django.db.models.base import Model

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length= 100 ) 
    cnpj = models.CharField(max_length= 14 )
    cep = models.CharField(max_length= 9 )
    endereco = models.CharField(max_length= 100 ) 
    numero = models.CharField(max_length= 6 )
    bairro = models.CharField(max_length= 100 )
    municipio = models.CharField(max_length= 50 )
    estado = models.CharField(max_length= 100 )
    email = models.CharField(max_length= 100 )
    senha = models.CharField(max_length= 50 )
    confsenha =  models.CharField(max_length= 50,blank=True )
    

#class Publicar(models.Model):
    #publicacao = models.CharField(max_length=500)
   
