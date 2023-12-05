# views.py
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from magazijn.models import ProductItem
from directie.filters import DateFilter

class PCRapportage(LoginRequiredMixin, View):
    product_item_model = ProductItem
    date_filter = DateFilter
    template_name = 'directie/product-categorie-rapportage.html'

    def get(self, request, id, *args, **kwargs):
        product_items = self.product_item_model.objects.filter(product__catagorieën__id=id)

        date_filter = self.date_filter(request.GET, queryset=product_items)

        # Use the filtered queryset
        product_items = date_filter.qs

        context = {
            'product_items': product_items,
            'date_filter': date_filter,
        }

        return render(request, self.template_name, context)