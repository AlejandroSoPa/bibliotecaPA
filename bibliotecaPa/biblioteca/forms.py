from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuari, Centre
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

        self.fields['first_name'].label = 'Nom'
        self.fields['last_name'].label = 'Cognoms'

class CustomCreateUserForm(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = ('username', 'email', 'first_name', 'last_name', 'data_naixement', 'centre') 

    def __init__(self, *args, **kwargs):
        # Obtener el centro pasado como argumento
        centro = kwargs.pop('centre', None)

        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['data_naixement'].required = True
        self.fields['centre'].widget.attrs['hidden'] = True
        self.fields['data_naixement'].widget = DateInput(attrs={'type': 'date'})

        self.fields['centre'].label = ''

        self.fields['username'].label = 'Nom d\'usuari'
        self.fields['email'].label = 'Correu electrònic'
        self.fields['first_name'].label = 'Nom'
        self.fields['last_name'].label = 'Cognoms'

        # Asignar el centro al campo centre si se proporciona
        if centro:
            self.fields['centre'].initial = centro

class CSVUploadForm(forms.Form):
    centre = forms.ModelChoiceField(queryset=Centre.objects.all(), label='Centro')
    archivo_csv = forms.FileField(label='Seleccionar archivo CSV')

    def __init__(self, *args, **kwargs):
        centro = kwargs.pop('centre', None)
        super().__init__(*args, **kwargs)
        self.fields['centre'].widget.attrs['hidden'] = True
        self.fields['centre'].label = ''

        if centro:
            self.fields['centre'].initial = centro