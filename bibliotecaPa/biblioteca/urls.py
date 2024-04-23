from django.contrib import admin
from django.urls import path
from . import api
from biblioteca.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login_view, name='index'),  # Esta es la ruta por defecto, si accedes a la raíz del sitio.
    path('dashboard/', dashboard, name='dashboard'),
    path('api/hello/', api.hello, name='hello'),
    path('logout/', logout_view, name='logout'),
]