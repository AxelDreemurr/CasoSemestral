from django.urls import path
from .views import index, about, login, productos

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('productos/', productos, name="productos"),
]