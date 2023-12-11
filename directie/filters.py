import django_filters
from django import forms
from magazijn.models import ProductItem, Product, Catagorie, Pakket
from directie.models import Leverancier
from klanten.models import Klant

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


    product_category = django_filters.ModelMultipleChoiceFilter(queryset=Catagorie.objects.all(),
                                                                field_name='product__catagorieën',
                                                                to_field_name='id',
                                                                label='Product categorie',
                                                                widget=forms.CheckboxSelectMultiple,)
    class Meta:
        model = ProductItem
        fields = []
    

class DateFilter2(django_filters.FilterSet):
    month = django_filters.NumberFilter(field_name='leverings_datum__month', label='Month')
    year = django_filters.NumberFilter(field_name='leverings_datum__year', label='Year')
    
    product_category = django_filters.ModelMultipleChoiceFilter(queryset=Catagorie.objects.all(),
                                                                field_name='product__catagorieën',
                                                                to_field_name='id',
                                                                label='Product categorie',
                                                                widget=forms.CheckboxSelectMultiple,)

    adres = django_filters.ModelMultipleChoiceFilter(queryset= Klant.objects.all(),
                                                     field_name='pakket__gezinsnaam', 
                                                     label='postcode',
                                                     to_field_name='id',
                                                     widget=forms.CheckboxSelectMultiple,
                                                     )

    



    class Meta:
        model = ProductItem
        fields = []