"""
URL configuration for bibliotecaPa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from biblioteca.views import *
from biblioteca import api
from django.contrib.auth import views as auth_views
from biblioteca import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='index'),  # Esta es la ruta por defecto, si accedes a la raíz del sitio.
    path('dashboard/', dashboard, name='dashboard'),
    path('api/hello/', api.hello, name='hello'),
    path('logout/', logout, name='logout'),
    path('reset-password/', password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('', include('biblioteca.urls'))
]