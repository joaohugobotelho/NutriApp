from django.shortcuts import render, redirect
from .models import Usuario
from .calculos import calcular_calorias_usuario
from .forms import UsuarioForm

def usuario_dieta(request):
    usuario = Usuario.objects.first()

    calorias = None

    if usuario:
        calorias = int(calcular_calorias_usuario(usuario))

    return render(request, 'usuarios/dieta.html', {
        'usuario': usuario,
        'calorias': calorias
    })


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dieta/')

    else:
        form = UsuarioForm()

        return render(request, 'usuarios/cadastro.html', {'form': form})