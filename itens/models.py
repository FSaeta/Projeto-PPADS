from django.db import models
from django.urls.base import reverse

from datetime import datetime
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField("Categoria", max_length=255)
    def __str__(self):
        return self.nome

class Itens(models.Model):
    data_criacao = models.DateField("Data de Criação", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, verbose_name="usuario", null=True)
    
    titulo = models.CharField("Título", max_length=100, unique=True)
    pais = models.CharField("Pais", max_length=100)
    ano_lancamento = models.IntegerField("Ano de Lançamento", default=datetime.now().year)
    categoria = models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.SET_NULL, null=True)
    tipo = models.CharField("Tipo", max_length=100)
    ativo = models.BooleanField("Ativo", default=False)
    
    class Meta:
        abstract = True
    
    def aprovar_cadastro(self, user):
        if user.is_superuser:
            self.ativo = True
            self.save()

    def excluir_cadastro(self, user):
        if user.is_superuser:
            self.delete()

class Livro(Itens):
    volume = models.PositiveSmallIntegerField("Volume")
    autor = models.CharField("Autor", max_length=100)
    editora = models.CharField("Editora", max_length=100)

    def get_absolute_url(self):
        return reverse("itens:livro", kwargs={'pk': self.pk})

class Filme(Itens):
    volume = models.PositiveSmallIntegerField("Volume", null=True)
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

    def get_absolute_url(self):
        return reverse("itens:filme", kwargs={'pk': self.pk})

class Serie(Itens):
    qtd_temporadas = models.PositiveSmallIntegerField("Número de temporadas")
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

    def get_absolute_url(self):
        return reverse("itens:serie", kwargs={'pk': self.pk})