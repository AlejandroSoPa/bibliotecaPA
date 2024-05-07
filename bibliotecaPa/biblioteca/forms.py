from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuari, Centre, Prestec, Article
from django.forms.widgets import DateInput
from django.utils import timezone
from datetime import timedelta

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
        self.fields["imatge"].label = "Imatge de perfil"

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

class CustomCreatePrestec(forms.ModelForm):
    class Meta:
        model = Prestec
        fields = ('usuari', 'article', 'data_préstec','data_retorn')
    def __init__(self,  *args, **kwargs):
        user_centre = kwargs.pop('user_centre', None)
        print(user_centre)
        super().__init__(*args, **kwargs)
        self.fields['usuari'].label = 'Usuari'
        self.fields['article'].label = 'Article'
        self.fields['data_préstec'].label = 'Data de préstec'
        self.fields['data_retorn'].label = 'Data de retorn'

        min_date = timezone.now() + timedelta(days=7)

        self.fields['data_préstec'].widget = forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')})
        self.fields['data_retorn'].widget = forms.DateInput(attrs={'type': 'date', 'min': min_date.strftime('%Y-%m-%d')})

        # Filter users based on the user's centre
        if user_centre:
            self.fields['usuari'].queryset = Usuari.objects.filter(centre=user_centre)

                # Filter articles based on availability
        available_articles = Article.objects.filter(ejemplares__gt=0)
        self.fields['article'].queryset = available_articles
