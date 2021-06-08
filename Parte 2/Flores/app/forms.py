from django import forms
from django.forms import ModelForm, fields
from .models import producto
from django.contrib.auth.forms import UserCreationForm        
from django.contrib.auth.models import User

class productoForm(ModelForm):
    
    nombre = forms.CharField(min_length=3,max_length=200)
    precio = forms.IntegerField(min_value=10, max_value=100000)
    
    class Meta:
        model = producto
        fields = ['nombre', 'precio', 'tipo', 'imagen']

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


