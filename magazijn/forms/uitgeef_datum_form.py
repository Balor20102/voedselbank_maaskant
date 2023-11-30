from django import forms
from magazijn.models import Pakket

class UitgeefDatumForm(forms.ModelForm):
    uitgiftdatum = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Uitgiftdatum',)
    class Meta:
        model = Pakket
        fields = ['uitgiftdatum']