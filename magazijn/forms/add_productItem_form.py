from django import forms
from magazijn.models import ProductItem
from directie.models import Leverancier

class AddProductItemForm(forms.ModelForm):
    voorraad = forms.IntegerField(required=True)
    leverancier = forms.ModelChoiceField(queryset=Leverancier.objects.all(), required=True)
    houdsbaarheiddatum = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ProductItem
        fields = ['voorraad','leverancier', 'houdsbaarheiddatum']


class updateProductItemForm(forms.ModelForm):
    leverancier = forms.ModelChoiceField(queryset=Leverancier.objects.all(), required=True)
    houdsbaarheiddatum = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    status = forms.ChoiceField(choices=ProductItem.STATUS_CHOICES, required=True)

    class Meta:
        model = ProductItem
        fields = ['leverancier', 'houdsbaarheiddatum']


class StockAddProductItemForm(forms.ModelForm):
    leverancier = forms.ModelChoiceField(queryset=Leverancier.objects.all(), required=True)
    houdsbaarheiddatum = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ProductItem
        fields = ['leverancier', 'houdsbaarheiddatum']