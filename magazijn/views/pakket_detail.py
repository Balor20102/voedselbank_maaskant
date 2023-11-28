from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from ..filters import ProductFilter, CategorieProduct
from magazijn.models import Pakket, ProductItem, Product
from klanten.models import Klant

class PakketDetailView(LoginRequiredMixin, View):
    template_name = "magazijn/pakket-detail.html"
    pakket_model = Pakket
    product_model = Product
    product_item_model = ProductItem
    filterset_product = ProductFilter
    filterset_categorie = CategorieProduct

    def get(self, request, id):
        pakket = get_object_or_404(Pakket, pk=id)

        klant = get_object_or_404(Klant, pk=pakket.gezinsnaam.id)

        product_items = self.product_item_model.objects.filter(pakket=pakket)
        product_counts = product_items.values('product').annotate(count=Count('product'))

        context = {
            'pakket': pakket,
            'product_items': product_items,
            'product_counts': product_counts,
            'klant': klant,
        }

        for product_count in product_counts:
            product = self.product_model.objects.get(pk=product_count['product'])
            product_count['product'] = product


        return render(request, self.template_name, context)

