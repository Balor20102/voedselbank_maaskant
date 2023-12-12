from django import forms
from ..models import Product, Catagorie

class ProductForm(forms.ModelForm):
    catagorieën = forms.ModelMultipleChoiceField(queryset=Catagorie.objects.all(), widget=forms.CheckboxSelectMultiple ,required=False)
    afbeelding = forms.ImageField()
    class Meta:
        model = Product
        fields = ['name', 'EAN', 'afbeelding', 'varkesvlees', 'vegataries', 'veganistisch','catagorieën', 'voorraad']

class UpdateProductForm(forms.ModelForm):
    catagorieën = forms.ModelMultipleChoiceField(queryset=Catagorie.objects.all(), widget=forms.CheckboxSelectMultiple ,required=False)
    afbeelding = forms.ImageField()
    class Meta:
        model = Product
        fields = ['name', 'EAN', 'afbeelding', 'varkesvlees', 'vegataries', 'veganistisch','catagorieën']