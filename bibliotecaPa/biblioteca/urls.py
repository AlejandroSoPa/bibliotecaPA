from django.contrib import admin
from django.urls import path
from . import api
from biblioteca.views import *
from .views import password_reset_request, password_reset_confirm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', login_view, name='index'),  # Esta es la ruta por defecto, si accedes a la raíz del sitio.
    path('dashboard/', dashboard, name='dashboard'),
    path('api/hello/', api.hello, name='hello'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('reset-password/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/', password_reset_request, name='password_reset_request'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

]
