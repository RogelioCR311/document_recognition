# forms.py
from django import forms
from .models import Documents

class UserDocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['identification', 'curp', 'rfc']
