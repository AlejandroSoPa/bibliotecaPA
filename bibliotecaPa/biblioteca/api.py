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