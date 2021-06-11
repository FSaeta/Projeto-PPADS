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

# Relatórios
def get_num_medio_amigos():
    total_users = Usuario.objects.all().count()
    total_amigos = 0
    for user in Usuario.objects.all():
        total_amigos += user.amigos.all().count()
    media = total_amigos / total_users
    return {'media': media, 'amigos':total_amigos}

class RelatorioMediaAmigos():
    def __init__(self):
        values = get_num_medio_amigos()
        self.total_users = Usuario.objects.all().count()
        self.media = values['media']
        self.total_amigos = values['amigos']

class ItemRelatorioMaisConectado():

    def __init__(self, pos, user, q_amigos):
        self.pos = pos
        self.user = user
        self.qtd_amg = q_amigos

class RelatorioMaisConectados():

    def __init__(self):
        kw = self.get_membros_mais_conectados()
        if len(kw.keys()) >= 1:
            self.um     = ItemRelatorioMaisConectado(1, kw['1']['user'], kw['1']['num_amigos'])
        if len(kw.keys()) >= 2:
            self.dois   = ItemRelatorioMaisConectado(2, kw['2']['user'], kw['2']['num_amigos'])
        else:
            self.dois = None
        if len(kw.keys()) >= 3:
            self.tres   = ItemRelatorioMaisConectado(3, kw['3']['user'], kw['3']['num_amigos'])
        else:
            self.tres = None
        if len(kw.keys()) >= 4:
            self.quatro = ItemRelatorioMaisConectado(4, kw['4']['user'], kw['4']['num_amigos'])
        else:
            self.quatro = None
        if len(kw.keys()) >= 5:
            self.cinco  = ItemRelatorioMaisConectado(5, kw['5']['user'], kw['5']['num_amigos'])
        else:
            self.cinco = None
        if len(kw.keys()) >= 6:
            self.seis   = ItemRelatorioMaisConectado(6, kw['6']['user'], kw['6']['num_amigos'])
        else:
            self.seis = None
        if len(kw.keys()) >= 7:
            self.sete   = ItemRelatorioMaisConectado(7, kw['7']['user'], kw['7']['num_amigos'])
        else:
            self.sete = None
        if len(kw.keys()) >= 8:
            self.oito   = ItemRelatorioMaisConectado(8, kw['8']['user'], kw['8']['num_amigos'])
        else:
            self.oito = None
        if len(kw.keys()) >= 9:
            self.nove   = ItemRelatorioMaisConectado(9, kw['9']['user'], kw['9']['num_amigos'])
        else:
            self.nove = None
        if len(kw.keys()) >= 10:
            self.dez   = ItemRelatorioMaisConectado(10,kw['10']['user'], kw['10']['num_amigos'])
        else:
            self.dez = None
        
    def get_membros_mais_conectados(self):
        membros = [user for user in Usuario.objects.all()]
        mais_conectados = {}
        if len(membros) < 10:
            x = len(membros)
        else:
            x = 10

        for n in range(0,x):
            maior = 0
            maior_user = None
            for membro in membros:
                if membro.amigos.all().count() >= maior:
                    maior = membro.amigos.all().count()
                    maior_user = membro
            mais_conectados.update({str(n+1): {'user': maior_user, 'num_amigos': maior}})
            membros.remove(maior_user)
        return mais_conectados
    
    def gerar_relatorio(self):
        fields = [self.um,self.dois,self.tres,self.quatro,self.cinco,self.seis,self.sete,self.oito,self.nove,self.dez]
        iter_fields = []
        for field in fields:
            if field:
                iter_fields.append(field)
        return iter_fields

def relatorios(request):
    context = {}
    if not request.user.is_superuser:
        return redirect('/')
    num_medio_amigos = RelatorioMediaAmigos()
    mais_conectados = RelatorioMaisConectados()

    context.update({
        'rel_media_amigos': num_medio_amigos,
        'rel_mais_conectados': mais_conectados,
    })
    return render(request, 'relatorios.html', context)

