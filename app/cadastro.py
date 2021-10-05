
from django.db.models.base import Model
from django.forms import ModelForm
from app.models import Cadastro

class CadastroForm(ModelForm):
    class Meta:
      model = Cadastro
      fields = ['nome','cnpj','cep', 'endereco','numero','bairro','municipio', 'estado', 'email', 'senha', 'confsenha']  