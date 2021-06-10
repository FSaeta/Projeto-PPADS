from os import name
from pyUFbr.baseuf import ufbr

def choice_cidades():
    lista_cidades = []
    for es in ufbr.list_uf:
        cont = 0
        for cidade in ufbr.list_cidades(es):
            tupla_cidade = (es+str(cont), cidade)
            lista_cidades.append(tupla_cidade)
            cont += 1
    return lista_cidades

def choice_estados():
    estados = []
    for estado in ufbr.list_uf:
        estados.append((estado, estado))
    return estados

CIDADES = choice_cidades()
ESTADOS = choice_estados()

if __name__ == '__main__':
    print(ESTADOS)
    print(CIDADES)

def get_users_context(request):
    usuarios_solicitados = [p.user_recebido for p in request.user.user_enviado.filter(aceito=False)]
    usuarios_enviados = [p.user_enviado for p in request.user.user_recebido.filter(aceito=False)]

    values = {
        'buscando': False,
        'usuarios_solicitados': usuarios_solicitados,
        'usuarios_enviados': usuarios_enviados,
    }
    return values

