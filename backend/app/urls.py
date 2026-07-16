from django.urls import path
from .views import hello_world, cache_test

urlpatterns = [
    path("hello/", hello_world, name="hello_world"),
    path("cache/", cache_test, name="cache_test"),
]