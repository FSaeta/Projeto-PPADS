from itens.forms import CadastroFilme
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import CadastroFilme, CadastroSerie, CadastroLivro

def index(request):
    context = {}

    context.update({
        'itens': [1,2,3,4,5]
    })

    return render(request, 'index.html', context)

def itens(request, tipo_item):
    context = {}
    context['tipo_item'] = tipo_item
    if tipo_item == 'filme':
        classe_item = Filme
        item_name = 'Filme'
        plural_item_name = 'Filmes'

    elif tipo_item == 'livro':
        classe_item = Livro
        item_name = 'Livro'
        plural_item_name = 'Livros'

    elif tipo_item == 'serie':
        classe_item = Serie
        item_name = 'Série'
        plural_item_name = 'Séries'
    else:
        return redirect('/')

    itens_objs = classe_item.objects.filter(ativo=True)

    context.update({
        'itens': itens_objs,
        'item_name': item_name,
        'plural_item_name': plural_item_name,
    })

    return render(request, 'itens.html', context)

def item(request, tipo_item, pk):
    context = {}
    context['tipo_item'] = tipo_item

    if tipo_item == 'filme':
        classe_item = Filme
        item_name = 'Filme'
        plural_item_name = 'Filmes'

    elif tipo_item == 'livro':
        classe_item = Livro
        item_name = 'Livro'
        plural_item_name = 'Livros'

    elif tipo_item == 'serie':
        classe_item = Serie
        item_name = 'Série'
        plural_item_name = 'Séries'
    else:
        return redirect('/')

    item_obj = get_object_or_404(classe_item, id=pk)
    context.update({
        'item': item_obj,
        'item_name': item_name,
        'plural_item_name': plural_item_name,
    })
    return render(request, 'item.html', context)

def cadastrar_item(request, tipo_item):
    context = {}
    context['tipo_item'] = tipo_item

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
    else:
        return redirect('/')
    
    if request.method == 'POST':
        values_post = {}
        for k, v in request.POST.items():
            values_post.update({k:v})
        values_post['user_id'] = request.user.id
        values_post['tipo'] = tipo_item
        
        if tipo_item == 'filme':
            form = CadastroFilme(values_post)
        elif tipo_item == 'livro':
            form = CadastroLivro(values_post)
        elif tipo_item == 'serie':
            form = CadastroSerie(values_post)
        import pdb; pdb.set_trace()
        
        if form.is_valid():
            form.save()
            context['mensagem_status'] = "Cadastro realizado com sucesso !"
        else:
            context['erro'] = True
            context['mensagem_status'] = "Algo está errado com o seu cadastro !"

    context.update({
        'form': form,
        'item_name': item_name,
        'plural_item_name': plural_item_name,
    })
    return render(request, 'cadastro_item.html', context)
