from django.urls import path

from .views import *

urlpatterns = [
    path('avaliar/<str:tipo_item>/<int:item_id>/', avaliar_item, name='avaliar_item'),
    path('<str:tipo_item>/<int:pk>/', avaliacao, name="avaliacao"),
]
