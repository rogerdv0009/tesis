from django import forms
from .models import Prevencion, Reporte
# forms.py

from django.contrib.auth.models import User
from django import forms


class PrevencionForm(forms.ModelForm):
    class Meta:
        model = Prevencion
        fields = '__all__'

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = '__all__'