from django.contrib import admin
from .models import producto, tipo_producto 
from .forms import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'tipo']
    search_fields = ['nombre']
    list_per_page = 4
    form = productoForm
    

admin.site.register(tipo_producto)
admin.site.register(producto, ProductoAdmin)