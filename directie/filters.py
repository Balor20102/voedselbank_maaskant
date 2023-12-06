import django_filters
from django import forms
from magazijn.models import ProductItem, Product
from directie.models import Leverancier

class DateFilter(django_filters.FilterSet):
    month = django_filters.NumberFilter(field_name='leverings_datum__month', label='Month')
    year = django_filters.NumberFilter(field_name='leverings_datum__year', label='Year')
    leverancier = django_filters.ModelMultipleChoiceFilter(
        queryset=Leverancier.objects.all(), 
        field_name='leverancier',
        label='Leverancier', 
        to_field_name='id',
        widget=forms.CheckboxSelectMultiple,
        
        )
    product = django_filters.ModelMultipleChoiceFilter(
        queryset=Product.objects.all(),
        field_name='product',
        label='Product', 
        to_field_name='id',
        widget=forms.CheckboxSelectMultiple,
        )

    class Meta:
        model = ProductItem
        fields = []
    
    