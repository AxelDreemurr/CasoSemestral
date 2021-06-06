from django.db import models

# Create your models here.
class tipo_producto(models.Model):
    tipo = models.CharField(max_length=80)
    
    def __str__(self):
        return self.tipo
        
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    tipo = models.ForeignKey(tipo_producto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.nombre
    #python manage.py makemigrations --> CREA ARCHIVO MIGRATIONS
    #python manage.py migrate --> ENVIA EL ARCHIVO A LA BD
    #python manage.py createsuperuser --> CREA EL ADMIN DE LA WEB