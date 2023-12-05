import django_filters
from magazijn.models import ProductItem

class DateFilter(django_filters.FilterSet):
    month = django_filters.NumberFilter(field_name='leverings_datum__month', label='Month')
    year = django_filters.NumberFilter(field_name='leverings_datum__year', label='Year')

    class Meta:
        model = ProductItem
        fields = []
    
    