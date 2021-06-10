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
            avaliacao = Avaliacao.objects.filter(user_id=request.user.id).order_by('-create_date').first()
            return redirect(f'/avaliacoes/{tipo_item}/{avaliacao.id}')
        else:
            context['erro'] = True
            context['mensagem_status'] = "Algo está errado com o seu cadastro !"
        context['form'] = form

    context.update({
        'item': item_obj,
    })
    return render(request, 'avaliar_item.html', context)


def avaliacao(request, tipo_item, pk):
    context = {}
    if tipo_item not in ('filme', 'livro', 'serie'):
        return redirect('/')
    context.update(get_avaliacoes_context(tipo_item))

    avaliacao = get_object_or_404(Avaliacao, id=pk)
    context['avaliacao'] = avaliacao
    form_comentario = context['classe_form_comentario'](avaliacao, request.user)

    if request.method == 'POST':
        if 'curtir_avaliacao' in request.POST:
            avaliacao.curtir(request.user)
        elif 'descurtir_avaliacao' in request.POST:
            avaliacao.descurtir(request.user)
        elif 'comentar' in request.POST:
            form_comentario = context['classe_form_comentario'](avaliacao, request.user, request.POST)
            if form_comentario.is_valid():
                form_comentario.save()

        if 'from_card' in request.POST and 'single' not in request.POST:
            if 'usuario' in request.POST.get('redirect_url'):
                return redirect(request.POST.get('redirect_url')+'#Avaliacoes')
            elif 'biblioteca' in request.POST.get('redirect_url'):
                return redirect(request.POST.get('redirect_url')+'#Avaliacoes')

    comentarios = avaliacao.comentario_set.all().order_by('-data_criacao')

    context.update({
        'avaliacoes': Avaliacao.objects.filter(pk=avaliacao.pk).order_by('-likes_cont'),
        'single': True,
        'form_comentario': form_comentario,
        'comentarios':comentarios,
    })

    return render(request, 'avaliacao.html', context)