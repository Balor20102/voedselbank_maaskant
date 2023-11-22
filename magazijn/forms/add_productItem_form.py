from django import forms
from magazijn.models import ProductItem
from directie.models import Leverancier

class AddProductItemForm(forms.ModelForm):
    leverancier = forms.ModelChoiceField(queryset=Leverancier.objects.all(), required=True)
    houdsbaarheiddatum = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ProductItem
        fields = ['leverancier', 'houdsbaarheiddatum']


