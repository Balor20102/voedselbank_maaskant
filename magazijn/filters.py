import django_filters
from django.db.models import Q
from django import forms
from .models import Catagorie

class ProductFilter(django_filters.FilterSet):
    searchbar = django_filters.CharFilter(
        method='filter_search', 
        label='',
        widget=forms.TextInput(attrs={'class': 'zoekbak'})
        
        )
                                    
    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(EAN__iexact=value)
        )
class CategorieProduct(django_filters.FilterSet):
    catagorie = django_filters.ModelMultipleChoiceFilter(
        field_name='catagorieën',
        to_field_name='id',
        queryset=Catagorie.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Categorieën',
    )