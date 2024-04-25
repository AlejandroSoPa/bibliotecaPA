from django.http import JsonResponse
from .models import *

from rest_framework.decorators import api_view

def hello(request):
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

def searchItems(request):
    query = request.GET.get('searchItem')
    print(query)
    items = Article.objects.all()
    if query:
        items = items.filter(titol__icontains=query)
    items = list(items.values())
    return JsonResponse(items, safe=False)

#    items = Article.objects.filter(titol__icontains="Percy")  # Obtén todos los elementos de la tabla 'Article'
#    return JsonResponse(list(items.values()), safe=False)  # Convierte el queryset en una lista de diccionarios