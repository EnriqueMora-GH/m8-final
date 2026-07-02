from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from .models import Producto


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class FormularioInicioSesion(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
        labels = {
            'nombre': 'Nombre del producto',
            'descripcion': 'Descripción',
            'precio': 'Precio ($CLP)',
            'stock': 'Stock disponible',
            'imagen': 'URL de la imagen',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 1:
            raise forms.ValidationError("El precio debe ser mayor a $0.")
        return precio


class FormularioCarrito(forms.Form):
    cantidad = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        label="Cantidad"
    )

    def __init__(self, *args, max_stock=None, **kwargs):
        super().__init__(*args, **kwargs)
        if max_stock:
            self.fields['cantidad'].widget.attrs['max'] = max_stock
            self.fields['cantidad'].validators.append(
                MinValueValidator(1)
            )
