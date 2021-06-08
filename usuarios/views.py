from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import Usuario
from .forms import UsuarioCreateForm


def cadastro(request):
    context = {}
    if str(request.method) == 'POST':
        form = UsuarioCreateForm(request.POST, request.FILES)
        print(form.as_p())
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            context['messagem_erro'] = "Formulário com Erro"
    else:
        form = UsuarioCreateForm()
    context.update({'form': form})
    return render(request, 'cadastro.html', context)