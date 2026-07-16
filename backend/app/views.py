from django.http import JsonResponse
from django.core.cache import cache

def hello_world(request):
    return JsonResponse({"message": "Hola desde Django API!"})

def cache_test(request):
    visitas = cache.get("visitas", 0)
    visitas += 1
    cache.set("visitas", visitas, timeout=60)
    return JsonResponse({"visitas_cache": visitas})