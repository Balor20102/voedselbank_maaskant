# forms.py
from django import forms
from magazijn.models import Catagorie
from directie.models import Leverancier

class createcategorieënform(forms.ModelForm):
    class Meta:
        model = Catagorie
        fields = ['name']

class categorieënaanpassenform(forms.ModelForm):
    class Meta:
        model = Catagorie
        fields = ['name']


class createleveranciersform(forms.ModelForm):
    class Meta:
        model = Leverancier
        fields = ['bedrijfsnaam', 'adres', 'contactpersoon', 'telefoon', 'email', 'leveringsdatum', 'leveringsfrequentie']