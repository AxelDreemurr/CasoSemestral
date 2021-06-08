from django.contrib import admin
from .models import producto, tipo_producto 
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'tipo']
    search_fields = ['nombre']
    list_per_page = 4

admin.site.register(tipo_producto)
admin.site.register(producto, ProductoAdmin)