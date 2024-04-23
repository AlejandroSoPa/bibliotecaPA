from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from .utils import generarLog, subir_logs_a_bd 

# Create your views here.

def login_view(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = Usuari.objects.get(email=username)
            if check_password(password, user.password):
                generarLog(request, 'INFO', f"Inicio de sesión exitoso", ruta='/index', usuario=user)
                subir_logs_a_bd(request)

                login(request, user)
                return redirect("dashboard")  # Redirige al usuario a 'dashboard'
            else:
                generarLog(request, 'ERROR', f"Intento de inicio de sesión fallido - Contraseña incorrecta", ruta='/index', usuario=None)
                subir_logs_a_bd(request)
                data['error'] = True
                data['errorMsg'] = "El correo electrónico o la contraseña son incorrectos."
        except Usuari.DoesNotExist:
            generarLog(request, 'ERROR', f"Intento de inicio de sesión fallido - Usuario no encontrado", ruta='/index', usuario=None)
            subir_logs_a_bd(request)
            data['error'] = True
            data['errorMsg'] = "El correo electrónico o la contraseña son incorrectos."
    return render(request, "index.html", data)

def dashboard(request):
    if not request.user.is_authenticated:
        generarLog(request, 'FATAL', f"Ha fallado la redirección a la página de dashboard", ruta='/dashboard', usuario=None)
        subir_logs_a_bd(request)
        return redirect('index')
    generarLog(request, 'INFO', f"Inicio de sesión exitoso", ruta='/dashboard', usuario=request.user)
    subir_logs_a_bd(request)
    return render(request, 'dashboard.html', {'user':request.user})

@login_required
def logout_view(request):
    generarLog(request, 'INFO', f"Cierre de sesión exitoso", ruta='/dashboard', usuario=request.user)
    logout(request)
    return redirect("index")
