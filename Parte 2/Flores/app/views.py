from django.contrib.auth import authenticate
from django.core import paginator
from .forms import productoForm, SignUpForm
from django.shortcuts import redirect, render
from .models import producto
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def login(request):
    return render(request, 'app/login.html')

def productos(request):
    productoAll = producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productoAll, 8)
        productoAll = paginator.page(page)
    except:
        raise Http404
    
    datos = {
        'lista' : productoAll,
        'paginator' : paginator
    }
    return render(request, 'app/productos.html', datos)

def lista_productos(request):
    productoAll = producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productoAll, 8)
        productoAll = paginator.page(page)
    except:
        raise Http404
    
    datos = {
        'lista' : productoAll,
        'paginator' : paginator
    }
    return render(request, 'app/lista_productos.html', datos)

def agregar(request):
    datos = {
        'form' : productoForm()
    }
    
    if request.method == 'POST':
        formulario = productoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "¡Producto añadido!"

        datos['form'] = formulario

    return render(request, 'app/agregar.html', datos)

def modificar(request, id):
    product = producto.objects.get(id=id)
    datos = {
        'form' : productoForm(instance=product)
    }
    
    if request.method == 'POST':
        formulario = productoForm(data=request.POST, instance=product, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "¡Producto Modificado!"
            
        datos['form'] = formulario  
        
    return render(request, 'app/modificar.html', datos)

def eliminar(request, id):
    product = producto.objects.get(id=id)
    product.delete()
    
    return redirect(to="lista_productos")

def registro_usuario(request):
    datos = {
        'form' : SignUpForm()
    }

    if request.method == 'POST':
        formulario2 = SignUpForm(request.POST)
        if formulario2.is_valid():
            formulario2.save()
            usuario = authenticate(username=formulario2.cleaned_data["username"],password=formulario2.cleaned_data["password1"])
            return redirect(to='index')

    return render(request, 'registration/signup.html', datos)