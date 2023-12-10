from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def inicio(request):
    return render(request, 'canciones/inicio.html', {})

@login_required
def canciones(request):
    return render(request, 'canciones/canciones.html', {})


@login_required
def autores(request):
    return render(request, 'canciones/autores.html', {})
    

def exit(request):
    logout(request)
    return redirect('inicio')

