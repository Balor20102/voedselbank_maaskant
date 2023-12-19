from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Case, When, IntegerField
from magazijn.models import Product, ProductItem, Catagorie
from klanten.models import Klant

from directie.filters import DateFilter2


class UitgaatRapportage(LoginRequiredMixin, View):
    """Class-based view voor de uitgaat rapportage."""

    template_name = 'directie/uitgaat_rapportage.html'

    def get(self, request):
        
        # Alle producten
        product_items = ProductItem.objects.all() # haal alle product items op

        # Filter
        myFilter = DateFilter2(request.GET, queryset=product_items) # filter product items op datum

        products = myFilter.qs.values('product__catagorieën').annotate(
                Goed=Count(Case(When(status=1, then=1), output_field=IntegerField())),
                in_pakket=Count(Case(When(status=2, then=1), output_field=IntegerField())),
                Verlopen=Count(Case(When(status=3, then=1), output_field=IntegerField())),
                Verdwenen=Count(Case(When(status=4, then=1), output_field=IntegerField())),
                # Add more lines for additional statuses as needed
            ).order_by('product__catagorieën') # tel product items per product en status en groepeer op catagorie
        
        for product in products:
            if product['product__catagorieën'] != None: # check of catagorie niet leeg is
                product['product__catagorieën'] = Catagorie.objects.get(id=product['product__catagorieën']) # haal catagorie op

        context = {
            "myFilter": myFilter,
            'products': products,
            'product_counts': products.count(),
        }
        return render(request, self.template_name, context=context)