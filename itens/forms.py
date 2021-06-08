
from django import forms

from .models import Filme, Serie, Livro
    
class CadastroFilme(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'elenco', 'pais', 'ano_lancamento', 'categoria', 'tipo', 'user_id']
        labels = {'user_id': '', 'tipo': ''}
        
    def __init__(self, *args, **kwargs):
        super(CadastroFilme, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','tipo'):
                self.fields[field].required = False

class CadastroSerie(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['titulo', 'diretor', 'elenco', 'pais', 'ano_lancamento', 'qtd_temporadas', 'categoria', 'tipo', 'user_id']   
        labels = {'user_id': '', 'tipo': ''}

    def __init__(self, *args, **kwargs):
        super(CadastroSerie, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','tipo'):
                self.fields[field].required = False

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'volume', 'autor', 'editora', 'pais', 'ano_lancamento', 'categoria', 'tipo', 'user_id']                
        labels = {'user_id': '', 'tipo': ''}

    def __init__(self, *args, **kwargs):
        super(CadastroLivro, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','tipo'):
                self.fields[field].required = False