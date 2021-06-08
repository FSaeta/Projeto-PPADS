from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import Usuario
from .forms import UsuarioCreateForm


def cadastro(request):
    context = {}
    if str(request.method) == 'POST':
        form = UsuarioCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            context['messagem_erro'] = "Formulário com Erro"
    else:
        form = UsuarioCreateForm()
    context.update({'form': form})
    return render(request, 'cadastro.html', context)


def view_usuario(request, pk):
    context = {}
    usuario = Usuario.objects.get(pk=pk)
    amigos_comum = [amigo for amigo in usuario.amigos.all() if amigo in request.user.amigos.all()]
    if usuario in request.user.amigos.all():
        context['sao_amigos'] = True

    context.update({
        'usuario': usuario,
        'count_amigos_comum': len(amigos_comum)
    })

    return render(request, 'pagina_usuario.html', context)

def amigos(request):
    context = {}

    if request.method == 'POST':
        amigo = Usuario.objects.get(pk=request.POST.get('id_amigo'))
        if 'excluir_amigo' in request.POST:
            request.user.amigos.remove(amigo)

    amigos = request.user.amigos.all().order_by('username')
    context['amigos'] = amigos
    return render(request, 'amigos.html', context)

def pedidos_amizade(request):
    context = {}

    return render(request, 'pedidos_amizade.html', context)