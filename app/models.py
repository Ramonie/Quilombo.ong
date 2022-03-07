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
    
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




