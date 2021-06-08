from itens.forms import CadastroFilme
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import CadastroFilme, CadastroSerie, CadastroLivro

def get_itens_context(tipo_item):
    if tipo_item == 'filme':
        classe_item = Filme
        item_name = 'Filme'
        plural_item_name = 'Filmes'
        form = CadastroFilme()

    elif tipo_item == 'livro':
        classe_item = Livro
        item_name = 'Livro'
        plural_item_name = 'Livros'
        form = CadastroLivro()

    elif tipo_item == 'serie':
        classe_item = Serie
        item_name = 'Série'
        plural_item_name = 'Séries'
        form = CadastroSerie()
    
    values = {
        'tipo_item': tipo_item,
        'classe_item': classe_item,
        'item_name': item_name,
        'plural_item_name': plural_item_name,
        'form': form,
    }

    return values


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
    itens_objs = context['classe_item'].objects.filter(ativo=True)
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

def validar_cadastros(request):
    context = {}
    return render(request, 'validar_cadastros.html', context)