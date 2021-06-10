from .models import *
from .forms import FazerAvaliacaoFilme, FazerAvaliacaoLivro, FazerAvaliacaoSerie, NovoComentario


def get_avaliacoes_context(tipo_item):
    if tipo_item == 'filme':
        classe_item = Filme
        item_name = 'Filme'
        plural_item_name = 'Filmes'
        form = FazerAvaliacaoFilme()
    elif tipo_item == 'livro':
        classe_item = Livro
        item_name = 'Livro'
        plural_item_name = 'Livros'
        form = FazerAvaliacaoLivro()
    elif tipo_item == 'serie':
        classe_item = Serie
        item_name = 'Série'
        plural_item_name = 'Séries'
        form = FazerAvaliacaoSerie()
    
    classe_form_comentario = NovoComentario
    values = {
        'tipo_item': tipo_item,
        'classe_item': classe_item,
        'item_name': item_name,
        'plural_item_name': plural_item_name,
        'form': form,
        'classe_form_comentario': classe_form_comentario,
    }
    return values

