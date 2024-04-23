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

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'dashboard.html', {'user':request.user})

@login_required
def logout_view(request):
    logout(request)
    return redirect("index")

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                uid = urlsafe_base64_encode(str(user.pk).encode())
                token = default_token_generator.make_token(user)
                reset_link = request.build_absolute_uri('/reset-password/{}/{}'.format(uid, token))
                subject = 'Password Reset Request'
                message = render_to_string('reset_password_email.html', {
                    'reset_link': reset_link,
                })
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
                return redirect('password_reset_done')
            else:
                messages.error(request, 'No user with that email address.')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_request.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
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