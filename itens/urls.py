from django.urls import path

from .views import *

urlpatterns = [
    path('<str:tipo_item>/', itens, name='itens'),
    path('<str:tipo_item>/<int:pk>/', item, name='item'),
    path('cadastrar/<str:tipo_item>/', cadastrar_item, name='cadastrar_item'),
]
