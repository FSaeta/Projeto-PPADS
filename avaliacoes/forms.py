from django import forms

from itens.models import Filme, Serie, Livro
from .models import Avaliacao, Comentario

class FazerAvaliacaoFilme(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao', 'valor', 'user_id', 'filme', 'tipo']
        labels = {'user_id': '', 'filme': '', 'tipo': ''}
        
    def __init__(self, *args, **kwargs):
        super(FazerAvaliacaoFilme, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','filme','tipo'):
                self.fields[field].required = False

class FazerAvaliacaoLivro(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao', 'valor', 'user_id', 'livro', 'tipo']
        labels = {'user_id': '', 'livro': '', 'tipo': ''}
        
    def __init__(self, *args, **kwargs):
        super(FazerAvaliacaoLivro, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','livro','tipo'):
                self.fields[field].required = False

class FazerAvaliacaoSerie(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao', 'valor', 'user_id', 'serie', 'tipo']
        labels = {'user_id': '', 'serie': '', 'tipo': ''}
        
    def __init__(self, *args, **kwargs):
        super(FazerAvaliacaoSerie, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('user_id','serie','tipo'):
                self.fields[field].required = False

class NovoComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['avaliacao', 'comentario', 'user_id']
        labels = {'comentario': 'Comentário'}
        
    def __init__(self, avaliacao, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'avaliacao':
                self.fields[field].initial = avaliacao
                self.fields[field].widget = forms.HiddenInput()
            elif field == 'user_id':
                self.fields[field].initial = user
                self.fields[field].widget = forms.HiddenInput()