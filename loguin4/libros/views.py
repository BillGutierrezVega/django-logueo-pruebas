from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def inicio(request):
    return render(request, 'libros/inicio.html', {})


@login_required
def libros(request):
    return render(request, 'libros/libros.html', {})

def exit(request):
    logout(request)
    return redirect('inicio')