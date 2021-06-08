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
