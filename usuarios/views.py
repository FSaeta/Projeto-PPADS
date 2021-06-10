from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from .models import PedidosAmizade, Usuario
from .forms import UsuarioCreateForm, SetPasswordForm, EditarDadosForm


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
    if request.user.is_anonymous:
        return redirect('/login')

    if request.method == 'POST':
        if 'session_amigos' in request.POST:
            amigo = Usuario.objects.get(pk=request.POST.get('id_amigo'))
            if 'excluir_amigo' in request.POST:
                request.user.amigos.remove(amigo)
            elif 'adicionar_amigo' in request.POST:
                request.user.enviar_pedido_amizade(amigo)
        else:
            if 'excluir_amigo' in request.POST:
                request.user.amigos.remove(usuario)
            elif 'adicionar_amigo' in request.POST:
                request.user.enviar_pedido_amizade(usuario)
            elif 'editar_dados' in request.POST:
                request.user.atualizar_registro(request.POST)
                context['mensagem_status'] = "Dados Atualizados !"
            elif 'alterar_senha' in request.POST:
                form_alterar_senha = SetPasswordForm(request.user, request.POST)
                if form_alterar_senha.is_valid():
                    form_alterar_senha.save()
                    context['mensagem_status'] = "Senha Alterada !!"
                    return redirect('/login')
                else:
                    context['mensagem_status'] = "As senhas estão incorretas !"

    amigos_comum = [amigo for amigo in usuario.amigos.all() if amigo in request.user.amigos.all()]
    if usuario in request.user.amigos.all():
        context['sao_amigos'] = True
    
    usuarios_solicitados = [p.user_recebido for p in request.user.user_enviado.filter(aceito=False)]
    if usuario in usuarios_solicitados:
        context['pedido_enviado'] = True

    context.update({
        'usuario': usuario,
        'usuarios_solicitados': usuarios_solicitados,
        'amigos_comum': amigos_comum,
        'count_amigos_comum': len(amigos_comum),
        'form_editar_dados': EditarDadosForm(request.user),
        'form_alterar_senha': SetPasswordForm(request.user),
    })

    return render(request, 'pagina_usuario.html', context)

def amigos(request):
    context = {}
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'POST':
        amigo = Usuario.objects.get(pk=request.POST.get('id_amigo'))
        if 'excluir_amigo' in request.POST:
            request.user.amigos.remove(amigo)
        elif 'adicionar_amigo' in request.POST:
            request.user.enviar_pedido_amizade(amigo)

    usuarios_solicidados = [p.user_recebido for p in request.user.user_enviado.filter(aceito=False)]

    amigos = request.user.amigos.all().order_by('username')
    context.update({
        'amigos': amigos,
        'usuarios_solicidados': usuarios_solicidados,
    })
    return render(request, 'amigos.html', context)


def pedidos_amizade(request):
    context = {}
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'POST':
        pedido = PedidosAmizade.objects.get(pk=request.POST.get('id_pedido'))
        if 'recusar_pedido' in request.POST:
            pedido.recusar_pedido()
        elif 'aceitar_pedido' in request.POST:
            pedido.aceitar_pedido()

    pedidos = request.user.user_recebido.filter(aceito=False)
    context['pedidos'] = pedidos

    return render(request, 'pedidos_amizade.html', context)