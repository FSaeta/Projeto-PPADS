from django.urls import path

from .views import *

urlpatterns = [
    path('cadastrar/<str:tipo_item>/', cadastrar_item, name='cadastrar_item'),
    path('validar/<str:tipo_item>/', validar_cadastros, name="validar_cadastros"),
    path('<str:tipo_item>/', itens, name='itens'),
    path('<str:tipo_item>/<int:pk>/', item, name='item'),
]
