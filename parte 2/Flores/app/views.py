from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def login(request):
    return render(request, 'app/login.html')

def productos(request):
    return render(request, 'app/productos.html')
