from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .calculos import calcular_calorias_usuario, calcular_macros
from .forms import UsuarioForm
from .calculos import montar_dieta

def usuario_dieta(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    calorias = int(calcular_calorias_usuario(usuario))
    macros = calcular_macros(usuario)
    
    dieta = montar_dieta(usuario)

    return render(request,'usuarios/dieta.html', {
        'usuario': usuario,
        'calorias': calorias,
        'macros': macros,
        'dieta':dieta
    })

   

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('dieta', id=usuario.id)

    else:
        form = UsuarioForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})