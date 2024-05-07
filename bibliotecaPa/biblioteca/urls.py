from django.contrib import admin
from django.urls import path
from . import api
from biblioteca.views import *
from .views import password_reset_request, password_reset_confirm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login_view, name='index'),  # Esta es la ruta por defecto, si accedes a la raÃ­z del sitio.
    path('dashboard/', dashboard, name='dashboard'),
    path('api/hello/', api.hello, name='hello'),
    path('logout/', logout_view, name='logout'),
    path('reset-password/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/', password_reset_request, name='password_reset_request'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('change-password/', change_password, name='change_password'),
    path('edit_profile/<int:user_id>/', edit_profile, name='edit_profile'),
    path('search/', search, name='search'),
    path('api/searchItems/<str:itemSearch>', api.searchItems, name='searchItem'),
    path('usuaris/', manage_users, name='manage_users'),
    path('api/getUsers/<int:centre>', api.getUsers, name='getUsers'),
    path('api/editUser/<int:id>', api.editUser, name='editUser'),
    path('create_user/', create_user, name='create_user'),
    path('import_users/', import_users, name='import_users'),
    path('list_loan/', list_loan, name='list_loan'),
    path('api/returnLoan/<int:id>/', api.returnLoan, name='returnLoan'),
]
