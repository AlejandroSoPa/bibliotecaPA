from django.contrib import admin
from django.urls import path
from . import api
from biblioteca.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/hello/', api.hello, name='hello'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]