from .models import Avaliacao
from django.shortcuts import render, get_object_or_404, redirect
from .funcoes import get_avaliacoes_context

def avaliar_item(request, tipo_item, item_id):
    context = {}
    if tipo_item not in ('filme', 'livro', 'serie'):
        return redirect('/')
    context.update(get_avaliacoes_context(tipo_item))

    item_obj = get_object_or_404(context['classe_item'], id=item_id)

    if request.method == 'POST':
        values_post = {}
        for k, v in request.POST.items():
            values_post.update({k:v})
        values_post['user_id'] = request.user.id
        values_post[tipo_item] = item_obj.id
        values_post['tipo'] = tipo_item

        form = context['form'].__class__(values_post)
        if form.is_valid():
            form.save()
            context['mensagem_status'] = "Avaliação realizada com sucesso !"
        else:
            context['erro'] = True
            context['mensagem_status'] = "Algo está errado com o seu cadastro !"
        context['form'] = form

    context.update({
        'item': item_obj,
    })
    return render(request, 'avaliar_item.html', context)

def avaliacao(request, item_id, pk):
    context = {}

    avaliacao = get_object_or_404(Avaliacao, id=pk)
    context['avaliacao'] = avaliacao

    comentarios = avaliacao.comentarios_set.all()

    return render(request, 'avaliacoes.html', context)