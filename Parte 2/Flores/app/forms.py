from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields
from .models import producto
from django.contrib.auth.forms import UserCreationForm        
from django.contrib.auth.models import User
from .validators import TamañoMaximoValidator

class productoForm(ModelForm):
    
    nombre = forms.CharField(min_length=3,max_length=200)
    precio = forms.IntegerField(min_value=10, max_value=100000)
    
    class Meta:
        model = producto
        fields = ['nombre', 'precio', 'tipo', 'imagen']
        imagen = forms.ImageField(validators=[TamañoMaximoValidator(maxfile=4)])

        def clean_nombre(self):
            nom = self.cleaned_data['nombre']
            existe = producto.objects.filter(nombre__iexact=nom).exists()

            if existe:
                raise ValidationError("Este artículo ya existe.")

            return nom

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


