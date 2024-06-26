from django.http import JsonResponse
from .models import *
from django.db.models import Q
from django.utils import timezone

def hello(request):
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

def searchItems(request, itemSearch):
    # Busca los artículos que coincidan con el título o el autor
    if itemSearch == "" or itemSearch == "undefined":
        jsonData = list(Article.objects.all().values())
    else:
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

def getLoans(request, centre):
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

def returnLoan(request, id):
    # Devuelve un préstamo
    loan = Prestec.objects.get(id=id)
    loan.data_lliurament = timezone.now()
    loan.article.ejemplares += 1
    loan.save()
    loan.article.save()
    return JsonResponse({
            "status": "OK",
        }, safe=False)