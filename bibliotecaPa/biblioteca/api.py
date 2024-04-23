from django.http import JsonResponse
from .models import *

from rest_framework.decorators import api_view

def hello(request):
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

