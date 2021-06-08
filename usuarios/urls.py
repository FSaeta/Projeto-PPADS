from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('conta', minha_conta, name='minha_conta'),
    path('<int:pk>', view_usuario, name='usuario'),
    path('amigos', amigos, name='amigos'),
    path('pedidos-amizade', pedidos_amizade, name='pedidos_amizade'),
]
