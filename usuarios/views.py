from os import access
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import PedidosAmizade, Usuario
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

    if request.method == 'POST':
        if 'excluir_amigo' in request.POST:
            request.user.amigos.remove(usuario)
        elif 'adicionar_amigo' in request.POST:
            request.user.enviar_pedido_amizade(usuario)

    amigos_comum = [amigo for amigo in usuario.amigos.all() if amigo in request.user.amigos.all()]
    if usuario in request.user.amigos.all():
        context['sao_amigos'] = True
    
    usuarios_solicidados = [p.user_recebido for p in request.user.user_enviado.filter(aceito=False)]
    if usuario in usuarios_solicidados:
        context['pedido_enviado'] = True

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
    if request.method == 'POST':
        pedido = PedidosAmizade.objects.get(pk=request.POST.get('id_pedido'))
        if 'recusar_pedido' in request.POST:
            pedido.recusar_pedido()
        elif 'aceitar_pedido' in request.POST:
            pedido.aceitar_pedido()

    pedidos = request.user.user_recebido.filter(aceito=False)
    context['pedidos'] = pedidos

    return render(request, 'pedidos_amizade.html', context)