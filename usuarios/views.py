from django.shortcuts import render, redirect

from .models import PedidosAmizade, Usuario
from .forms import UsuarioCreateForm, SetPasswordForm, EditarDadosForm

from avaliacoes.models import Avaliacao

from .funcoes import get_users_context


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
    context.update(get_users_context(request))

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

    if usuario in context['usuarios_solicitados']:
        context['pedido_enviado'] = True

    context.update({
        'usuario': usuario,
        'amigos_comum': amigos_comum,
        'form_editar_dados': EditarDadosForm(request.user),
        'form_alterar_senha': SetPasswordForm(request.user),
        'count_amigos_comum': len(amigos_comum),
        'avaliacoes': Avaliacao.objects.filter(user_id=usuario).order_by('-likes_cont'),
    })

    return render(request, 'pagina_usuario.html', context)

def amigos(request):
    context = {}
    if request.user.is_anonymous:
        return redirect('/login')
    context.update(get_users_context(request))

    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'POST':
        amigo = Usuario.objects.get(pk=request.POST.get('id_amigo'))
        if 'excluir_amigo' in request.POST:
            request.user.amigos.remove(amigo)
        elif 'adicionar_amigo' in request.POST:
            request.user.enviar_pedido_amizade(amigo)
        elif 'aceitar_amigo' in request.POST:
            pedido = PedidosAmizade.objects.get(user_enviado=amigo, user_recebido=request.user, aceito=False)
            pedido.aceitar_pedido()
        elif 'recusar_amigo' in request.POST:
            pedido = PedidosAmizade.objects.get(user_enviado=amigo, user_recebido=request.user, aceito=False)
            pedido.recusar_pedido()

    elif request.method == 'GET':
        if 'buscar' in request.GET:
            busca = request.GET.get('busca', False)
            if busca:
                context['buscando'] = True
                context['valor_busca'] = busca
                amigos = Usuario.objects.filter(username__icontains=busca).order_by('username')

    if not context['buscando']:
        amigos = request.user.amigos.all().order_by('username')
    
    context.update({
        'amigos': amigos,
    })
    return render(request, 'amigos.html', context)


def pedidos_amizade(request):
    context = {}
    if request.user.is_anonymous:
        return redirect('/login')
    context.update(get_users_context(request))

    if request.method == 'POST':
        pedido = PedidosAmizade.objects.get(pk=request.POST.get('id_pedido'))
        if 'recusar_pedido' in request.POST:
            pedido.recusar_pedido()
        elif 'aceitar_pedido' in request.POST:
            pedido.aceitar_pedido()

    pedidos = request.user.user_recebido.filter(aceito=False)
    context['pedidos'] = pedidos

    return render(request, 'pedidos_amizade.html', context)