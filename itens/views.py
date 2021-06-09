from itens.forms import CadastroFilme
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import CadastroFilme, CadastroSerie, CadastroLivro
from .funcoes import get_itens_context


def index(request):
    context = {}

    context.update({
        'itens': [1,2,3,4,5]
    })

    return render(request, 'index.html', context)

def itens(request, tipo_item):
    context = {}
    if tipo_item not in ('filme', 'livro', 'serie'):
        return redirect('/')
    context.update(get_itens_context(tipo_item))
    itens_objs = context['classe_item'].objects.filter(ativo=True).order_by('data_criacao')
    context.update({
        'itens': itens_objs,
    })
    return render(request, 'itens.html', context)

def item(request, tipo_item, pk):
    context = {}
    if tipo_item not in ('filme', 'livro', 'serie'):
        return redirect('/')
    context.update(get_itens_context(tipo_item))

    item_obj = get_object_or_404(context['classe_item'], id=pk)
    
    context.update({
        'item': item_obj,
    })
    return render(request, 'item.html', context)

def cadastrar_item(request, tipo_item):
    context = {}
    if tipo_item not in ('filme', 'livro', 'serie'):
        return redirect('/')
    context.update(get_itens_context(tipo_item))
    
    if request.method == 'POST':
        values_post = {}
        for k, v in request.POST.items():
            values_post.update({k:v})
        values_post['user_id'] = request.user.id
        values_post['tipo'] = tipo_item

        form = context['form'].__class__(values_post)
        if form.is_valid():
            form.save()
            context['mensagem_status'] = "Cadastro realizado com sucesso !"
        else:
            context['erro'] = True
            context['mensagem_status'] = "Algo está errado com o seu cadastro !"
        context['form'] = form

    return render(request, 'cadastro_item.html', context)

def validar_cadastros(request, tipo_item):
    context = {}
    if tipo_item not in ('filme', 'livro', 'serie'):
        return redirect('/')
    context.update(get_itens_context(tipo_item))

    if request.method == 'POST':
        item = context['classe_item'].objects.get(id=request.POST.get('id_item'))
        if 'validar' in request.POST:
            item.aprovar_cadastro(request.user)
        elif 'excluir' in request.POST:
            item.excluir_cadastro(request.user)
    
    itens_objs = context['classe_item'].objects.filter(ativo=False).order_by('data_criacao')
    context.update({'itens': itens_objs})
    return render(request, 'validar_cadastros.html', context)