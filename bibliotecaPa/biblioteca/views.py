from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import LoginSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        print (username, password)
        try:
            user = Usuari.objects.get(email=username)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                data['error'] = True
                data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
        except:
            data['error'] = True
            data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
    return render(request, "index.html", data)

def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def logout(request):
    logout(request)
    return JsonResponse({'status': 'ok'})

