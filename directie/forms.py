# forms.py
from django import forms
from magazijn.models import Catagorie
from directie.models import Leverancier
from klanten.models import Klant
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class createcategorieënform(forms.ModelForm):
    class Meta:
        model = Catagorie
        fields = ['name']

class categorieënaanpassenform(forms.ModelForm):
    class Meta:
        model = Catagorie
        fields = ['name']


class createleveranciersform(forms.ModelForm):
    leveringsdatum = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Leverancier
        fields = ['bedrijfsnaam', 'adres', 'contactpersoon', 'telefoon', 'email', 'leveringsdatum']

class klantenaanpassenform(forms.ModelForm):
    class Meta:
        model = Klant
        fields = ['gezinsnaam', 'volwassenen', 'kinderen', 'babies', 'postcode', 'varkesvlees', 'vegataries', 'veganistisch', 'alergieën']

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Functie')
    username = forms.CharField(required=True, label='Gebruikersnaam')
    password1 = forms.CharField(required=True, widget=forms.PasswordInput, label='Wachtwoord')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput, label='Wachtwoord bevestigen')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('group',)

