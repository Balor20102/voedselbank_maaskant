# forms.py
from django import forms
from magazijn.models import Catagorie
from directie.models import Leverancier
from klanten.models import Klant

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