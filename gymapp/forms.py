from django import forms
from .models import ClienteGimnasio

class ClienteGimnasioForm(forms.ModelForm):
    class Meta:
        model = ClienteGimnasio
        fields = ['nombre', 'apellido', 'rut', 'edad', 'genero', 'telefono', 'email']
        