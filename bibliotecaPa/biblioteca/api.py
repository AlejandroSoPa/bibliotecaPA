from django.http import JsonResponse
from .models import *
from django.db.models import Q

def hello(request):
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

def searchItems(request, itemSearch):
    # Busca los artículos que coincidan con el título o el autor
    jsonData = list(Article.objects.filter(Q(titol__icontains=itemSearch) | Q(autor__icontains=itemSearch)).values())
    return JsonResponse({
            "status": "OK",
            "items": jsonData,
        }, safe=False)

def getUsers(request,centre):
    # Devuelve todos los usuarios
    jsonData = list(Usuari.objects.filter(centre=centre).values())
    return JsonResponse({
            "status": "OK",
            "users": jsonData,
        }, safe=False)

def editUser(request,id):
    # Edita un usuario
    user = Usuari.objects.get(id=id)
    user.admin = not user.admin
    user.save()
    return JsonResponse({
            "status": "OK",
        }, safe=False)