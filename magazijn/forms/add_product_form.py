from django import forms
from ..models import Product, Catagorie

class ProductForm(forms.ModelForm):
    Catagorieën = forms.ModelMultipleChoiceField(queryset=Catagorie.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Product
        fields = ['name', 'EAN', 'afbeelding', 'varkesvlees', 'vegataries', 'veganistisch','catagorieën', 'voorraad']