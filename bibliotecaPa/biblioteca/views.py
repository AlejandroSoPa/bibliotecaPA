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

# Create your views here.

def login_view(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = Usuari.objects.get(email=username)
            if user is not None:
                login(request, user)
                print(request.user)
                return redirect("dashboard")  # Redirige al usuario a 'dashboard'
            else:
                data['error'] = True
                data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
        except Usuari.DoesNotExist:
            data['error'] = True
            data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
    return render(request, "index.html", data)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect("index")

