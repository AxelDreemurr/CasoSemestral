from django import forms
from django.forms import ModelForm, fields
from .models import producto        

class productoForm(ModelForm):
    
    nombre = forms.CharField(min_length=3,max_length=200)
    precio = forms.IntegerField(min_value=10, max_value=100000)
    
    class Meta:
        model = producto
        fields = ['nombre', 'precio', 'tipo', 'imagen']

