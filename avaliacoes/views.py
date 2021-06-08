from .models import Avaliacao
from django.shortcuts import render, get_object_or_404

def avaliar_item(request, tipo_item, item_id):
    context = {}

    return render(request, 'avaliar_item.html', context)

def avaliacao(request, item_id, pk):
    context = {}

    avaliacao = get_object_or_404(Avaliacao, id=pk)
    context['avaliacao'] = avaliacao

    comentarios = avaliacao.comentarios_set.all()

    return render(request, 'avaliacoes.html', context)