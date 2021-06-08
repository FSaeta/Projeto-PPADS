from django.contrib import admin
from django.urls import path, include

from itens.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('biblioteca/', include('itens.urls')),
    path('usuario/', include('usuarios.urls')),
]
