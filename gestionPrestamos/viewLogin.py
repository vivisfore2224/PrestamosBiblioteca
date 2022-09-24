from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from gestionPrestamos.models import Estudiante
from django.contrib import messages


def iniciarSesion(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contrasenia=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre,password=contrasenia)
            if usuario is not None:
                try:
                    est=Estudiante.objects.get(email=usuario.email)
                    login(request, usuario)
                    return redirect('../listaLibrosEst')
                except Estudiante.DoesNotExist:
                    if usuario.is_superuser:
                        login(request, usuario)
                        return redirect('../listaLibros')
                    else:
                        messages.success(request, f'Acceso Denegado')
            else: 
                messages.success(request, f'Usuario no existe.')
        else:
            messages.success(request, f'Datos incorrectos.')
    
    form=AuthenticationForm()
    return render(request, "login.html", {"form":form})

def cerrarSesion(request):
    logout(request)
    return redirect('../')
