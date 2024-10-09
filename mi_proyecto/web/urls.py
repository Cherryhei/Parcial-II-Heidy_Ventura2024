#estas son las urls a utilizar para la aplicacion de productos

from django.urls import path
from . import views

urlpatterns = [
    path('holamundo', views.hola_mundo),
    path('', views.inicio)
]