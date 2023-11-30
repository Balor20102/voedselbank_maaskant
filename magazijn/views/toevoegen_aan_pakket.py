from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from ..filters import ProductFilter, CategorieProduct
from magazijn.models import Pakket, ProductItem, Product
from klanten.models import Klant

class ToevoegenPakketView(LoginRequiredMixin, View):
    pakket_model = Pakket
    product_model = Product
    product_item_model = ProductItem
    filterset_product = ProductFilter
    filterset_categorie = CategorieProduct

    def get(self, request, product, pakket, hoeveel):
        product = get_object_or_404(Product, pk=product)
        pakket = get_object_or_404(Pakket, pk=pakket)
        product_items = self.product_item_model.objects.filter(product=product, status = 1).order_by('houdsbaarheiddatum')
        for i, item in zip(range(hoeveel), product_items):
                item.pakket = pakket
                item.status = 2
                item.save()

        product.voorraad -= hoeveel
        product.save()
        return redirect('pakket', pk=pakket.gezinsnaam.pk)