from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuari

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuari
        fields = ('first_name', 'last_name', 'imatge')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Oculta el campo de contraseña y el mensaje "No password set"
        self.fields.pop('password')