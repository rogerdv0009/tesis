from django import forms
from .models import Prevencion, reporte
# forms.py

from django.contrib.auth.models import User
from django import forms
from .models import CustomUser

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_photo']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password','is_staff']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        if self.instance.pk is None:
            user_instance = User()
            usuario_instance = super().save(commit=False)
        else:
            user_instance = self.instance.user
            usuario_instance = self.instance
   

class PrevencionForm(forms.ModelForm):
    class Meta:
        model = Prevencion
        fields = '__all__'

class ReporteForm(forms.ModelForm):
    class Meta:
        model = reporte
        fields = '__all__'