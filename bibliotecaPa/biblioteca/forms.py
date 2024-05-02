from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuari
from django.forms.widgets import DateInput

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

class CustomCreateUserForm(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = ('username', 'email', 'first_name', 'last_name', 'data_naixement')  # Asegúrate de incluir 'username', 'email', 'first_name' y 'last_name'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['data_naixement'].required = True
        self.fields['data_naixement'].widget = DateInput(attrs={'type': 'date'})
