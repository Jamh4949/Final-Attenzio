from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profesor
        fields = [
            'nombre',
            'correo',
            'contraseña',
            'direccion',
            'departamento',
            'identificacion',
            'codigo_profesor',
            'telefono',
            'codigo_clase',
        ]
