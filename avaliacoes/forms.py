from django import forms

from itens.models import Filme, Serie, Livro
from .models import Avaliacao

class FazerAvaliacaoFilme(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao', 'valor', 'user_id', 'filme']
        labels = {'user_id': '', 'filme': ''}
        
    def __init__(self, *args, **kwargs):
        super(FazerAvaliacaoFilme, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','filme'):
                self.fields[field].required = False

class FazerAvaliacaoLivro(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao', 'valor', 'user_id', 'livro']
        labels = {'user_id': '', 'livro': ''}
        
    def __init__(self, *args, **kwargs):
        super(FazerAvaliacaoLivro, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','livro'):
                self.fields[field].required = False

class FazerAvaliacaoSerie(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao', 'valor', 'user_id', 'serie']
        labels = {'user_id': '', 'serie': ''}
        
    def __init__(self, *args, **kwargs):
        super(FazerAvaliacaoSerie, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','serie'):
                self.fields[field].required = False