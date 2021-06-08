from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('productos/', productos, name="productos"),
    path('lista_productos/', lista_productos, name="lista_productos"),    
    path('agregar/', agregar, name="agregar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('registro_usuario/', registro_usuario, name="registro_usuario")
]