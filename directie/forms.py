# forms.py
from django import forms
from magazijn.models import Catagorie

class createcategorieënform(forms.ModelForm):
    class Meta:
        model = Catagorie
        fields = ['name']
