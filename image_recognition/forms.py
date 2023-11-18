# forms.py
from django import forms
from .models import Documents
from django.forms.widgets import FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, EmailInput


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'email': EmailInput(attrs={'class': 'form-control', 'type': 'text'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Hacer todos los campos requeridos
        for field_name, field in self.fields.items():
            field.required = True

class UserIdForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['identification']

class UserCurpForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['curp']

class UserRfcForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['rfc']

class UserActaForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['acta']

class UserSeguroForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['seguro']