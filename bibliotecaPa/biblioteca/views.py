from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from .utils import generarLog, subir_logs_a_bd 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomUserChangeForm
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
                return redirect("dashboard")
		# data['info'] = True
                # data['errorMsg'] = "Inicio de sesion correcto, redireccionando..."
            else:
                generarLog(request, 'WARNING', f"Contraseñas incorrectas: Intento de inicio de sesión fallido - Contraseña incorrecta", ruta='/index', usuario=None)
                subir_logs_a_bd(request)
                data['warning'] = True
                data['errorMsg'] = "El correo electrónico o la contraseña son incorrectos."

        except Usuari.DoesNotExist:
            generarLog(request, 'WARNING', f"Usuari.DoesNotExist: Intento de inicio de sesión fallido - Usuario no encontrado", ruta='/index', usuario=None)
            subir_logs_a_bd(request)
            data['warning'] = True
            data['errorMsg'] = "El correo electrónico o la contraseña son incorrectos."

    return render(request, "index.html", data)

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def manage_users(request):
    return render(request, 'manage_users.html')

def dashboard(request):
    print(request.user)
    if not request.user.is_authenticated:
        generarLog(request, 'ERROR', f"Ha fallado la redirección a la página de dashboard", ruta='/dashboard', usuario=None)
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

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = Usuari.objects.filter(email=email).first()
            if user:
                uid = urlsafe_base64_encode(str(user.pk).encode())
                token = default_token_generator.make_token(user)
                reset_link = ('/reset-password/{}/{}'.format(uid, token))
                subject = 'Password Reset Request'
                message = render_to_string('reset_password_email.html', {
                    'reset_link': reset_link,
                })
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
                generarLog(request, 'ERROR', f"Ha fallado la redirección a la página de dashboard", ruta='/dashboard', usuario=None)
                subir_logs_a_bd(request)
                return redirect('password_reset_done')
            else:
                messages.error(request, 'No user with that email address.')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_request.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Usuari.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Usuari.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == "POST":
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            messages.success(request, 'Password has been reset successfully.')
            return redirect('dashboard')
        return render(request, 'password_reset_confirm.html')
    else:
        messages.error(request, 'Invalid password reset link.')
        return redirect('dashboard')    

@login_required
def change_password(request):
    data = {}
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            data['info'] = True
            data['infoMsg'] = "La contrasenya s'ha canviat correctament."
            return redirect('change_password')
        else:
            data['warning'] = True
            data['infoMsg'] = "No s'ha pogut canviar la contrasenya."
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def edit_profile(request, user_id):
    data = {}
    user_to_edit = get_object_or_404(Usuari, id=user_id)
    
    if not (request.user.id == user_id or request.user.centre.id == user_to_edit.centre.id):
        return HttpResponseForbidden("You are not allowed to edit this profile.")
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user_to_edit)
        if form.is_valid():
            form.save()
            data['info'] = True
            data['infoMsg'] = "Usuari editat correctament."
            if user_to_edit:
                return redirect('manage_users')
            else:
                return redirect('dashboard')
    else:
        form = CustomUserChangeForm(instance=user_to_edit)
    
    return render(request, 'edit_profile.html', {'form': form})

